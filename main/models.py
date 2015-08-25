from django.db import models
from django.core.validators import RegexValidator

from main.meta import *
# Create your models here.

class Student(models.Model):
	name = models.CharField(
		default='',
		max_length=50)
	grade = models.CharField(
		default='',
		max_length=1,
		choices=GradeChoice)
	department = models.CharField(
		default='',
		max_length=4,
		choices=DepartmentChoice)
	facebookname = models.CharField(
		default='',
		max_length=100)
	email = models.EmailField(
		default='',
		max_length=100)

	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone = models.CharField(
		validators=[phone_regex],
		blank=True,
		max_length=15)