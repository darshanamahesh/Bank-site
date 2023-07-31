from django import forms
from .models import Applicant, District, Branch, Material

class ApplicantForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=Applicant.GENDER_CHOICES, widget=forms.RadioSelect)
    # district = forms.ModelChoiceField(queryset=District.objects.all(), widget=forms.Select(attrs={'class': 'district-select'}))
    # branch = forms.ModelChoiceField(queryset=Branch.objects.none(), widget=forms.Select(attrs={'class': 'branch-select'}))
    materials_provided = forms.ModelMultipleChoiceField(queryset=Material.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Applicant
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['branch'].queryset = Branch.objects.none()

            # Set the 'district' field's attributes to include the class 'district-select'
            #self.fields['district'].widget.attrs.update({'class': 'district-select'})

            # Check if 'district' data is available in the form POST data
            if 'district' in self.data:
                try:
                    district_id = int(self.data.get('district'))
                    # Filter branches based on the selected district
                    self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id).order_by('name')
                except (ValueError, TypeError):
                   pass
            elif self.instance.pk:
                # Set the 'branch' queryset based on the instance's district (when editing an existing applicant)
                self.fields['branch'].queryset = self.instance.district.branch_set.order_by('name')
            else:
                # Fallback to an empty queryset for 'branch' (when the form is rendered initially)
                self.fields['branch'].queryset = Branch.objects.none()

        def clean(self):
            cleaned_data = super().clean()

            # Add any custom validation or clean-up logic here if needed.
            # For example, you can perform additional validation on the data or modify it before saving.

            return cleaned_data

