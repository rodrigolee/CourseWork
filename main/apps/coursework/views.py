from django.shortcuts import render, redirect, HttpResponse
import string
def index(request):
    return render(request, 'coursework/index.html')
# Create your views here.
def submit(request):
    context={
        'name': request.POST['name'],
        'description': request.POST['description']
    }
    return render(reqest, 'coursework/index.html', context)
