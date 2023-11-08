from django.shortcuts import render
<<<<<<< HEAD
# Create your views here.
def home(request):
=======

# Create your views here.
def index (request):
>>>>>>> 6a7581b35d56240cf3a535985dd6d48061747cb3
	return render(request, 'index.html',{})