from django.contrib import admin
from main.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
	list_display = (
		'name',
		'grade',
		'department',
		'facebookname',
		'email',
		'phone')
admin.site.register(Student,StudentAdmin)