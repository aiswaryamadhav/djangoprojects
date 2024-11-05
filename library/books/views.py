from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def addbooks(request):
    return render(request,'add.html')

def viewbooks(request):
    return render(request,'view.html')