from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def c1(request):
    return render(request,'core/c1.html')

def c2(request):
    return render(request,'core/c2.html')

