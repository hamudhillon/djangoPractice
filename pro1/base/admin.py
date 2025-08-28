from django.contrib import admin
from django import forms
from .models import *
# Register your models here.



class EmpAdminForm(forms.ModelForm):
    class Meta:
        model=emp
        fields='__all__'
        widgets={
            "address":forms.Textarea(attrs={"rows":5,"cols":60})
        }


class empAdmin(admin.ModelAdmin):
    list_display=("name",'phone','department','address')
    search_fields=('name','phone')
    list_filter=('department','phone')
    ordering=("name",)
    list_per_page=10
    form=EmpAdminForm
    actions=['assign_to_hr']


    def assign_to_hr(self,request,queryset):
        hr_dep,created=department.objects.get_or_create(name='HR')
        queryset.update(department=hr_dep)
    assign_to_hr.short_description="Assign selected emp to HR Department"




admin.site.register(emp,empAdmin)
admin.site.register(department)
admin.site.register(student)
admin.site.register(Profile)



admin.site.site_header="MY ADMIN"
admin.site.site_title="My admin"
admin.site.index_title='Welcome to blog'

