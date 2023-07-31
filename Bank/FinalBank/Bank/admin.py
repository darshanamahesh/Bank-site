from django.contrib import admin

from .models import District, Branch, AccountType,Applicant, Material

admin.site.register(District)
admin.site.register(Branch)
admin.site.register(Applicant)
admin.site.register(AccountType)
admin.site.register(Material)
# Register your models here.
