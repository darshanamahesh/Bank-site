from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Branch, District
from django.shortcuts import render, redirect
from .forms import ApplicantForm
from .models import Applicant

def home(request):
    districts = District.objects.all()
    return render(request, 'home.html', {'districts': districts})

def district_wikipedia(request, district_id):
    return redirect('https://en.wikipedia.org/')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('applicant_form')
        else:
            messages.info(request, "InValid credentials")
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "user taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                return redirect('login')
                print("user created")
        else:
            messages.info(request, "wrong password")
            return redirect('register')
        return redirect('/')

    return render(request, 'register.html')


def applicant_form_view(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or another view after successful form submission
            return redirect('success')
        else:
            print(form.errors)
    else:
        form = ApplicantForm()

    return render(request, 'customer_form.html', {'form': form})

def success(request):

    return render(request, 'success.html')

# def get_branches(request, district_id):
#     branches = Branch.objects.filter(district_id=district_id).values('id', 'name')
#     return JsonResponse(list(branches), safe=False)
def get_branches_api(request):
    district_id = request.GET.get('district_id')
    try:
        district_id = int(district_id)
        branches = Branch.objects.filter(district_id=district_id).values('id', 'name')
        return JsonResponse({'branches': list(branches)})
    except (ValueError, TypeError):
        return JsonResponse({'branches': []})
def logout(request):
    auth.logout(request)
    return redirect('/')