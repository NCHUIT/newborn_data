from django import forms
from main.models import Student

class StudentForm(forms.ModelForm):
	"""docstring for StudentForm"""

	class Meta:
		model = Student 
		fields = '__all__'
    
		