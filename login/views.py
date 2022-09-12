from django.shortcuts import render

# Create your views here.
def login(request):
   # print(request.headers)
    return render(request, 'Login/login.html',{})
