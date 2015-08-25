from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.forms import StudentForm
# Create your views here.

def index(request):
	return render(request, 'main/index.html')

def student_new(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			user = form.save()
			return redirect('student_new_success')
	else:
		form = StudentForm()
	return render(request, 'main/student_new.html', 
		{'form' : form})

def student_new_success(request):
	return HttpResponse('Hello Success')