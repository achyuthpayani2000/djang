from django.shortcuts import render

# Create your views here.
def home(request):
   # print(request.headers)
    return render(request, 'home/home.html',{})
def about(request):
    return render(request,'home/about.html',{})

def help(request):
    return render(request,'home/help.html',{})
