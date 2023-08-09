from django.contrib import admin
from .models import Year,Student
# Register your models here.

admin.site.register(Year)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','year','blood_grp',)
    list_display_links = ('id','name',)
    ordering = ('id',)
admin.site.register(Student,StudentAdmin)
