import logging
from audioop import reverse

from django.contrib.auth.forms import UserCreationForm
from  django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect

# Create your views here.
import users
from home.views import home
from users.models import Users
UsersList=Users.objects.all()
def userlist(request):
    UsersList=Users.objects.all()
    print('UsersList')
    return render(request,'Users/userList.html',{'UserList':UsersList})

def useradd(request):
    if(request.method=='POST'):
        user=Users()
        user.username=request.POST.get('username')
        user.firstname=request.POST.get('firstname')
        user.lastname=request.POST.get('lastname')
        user.password=request.POST.get('password')
        user.persona=request.POST.get('persona')
        user.save()
        UsersList = Users.objects.all()
        return render(request,'Users/userList.html',{'UserList':UsersList})
    else:
        return render(request,'Users/register.html',{})

def userdetail(request,i):
    user=Users.objects.get(id=i)
    return render(request,'Users/userdetail.html',{'user':user})

def userdelete(request,i):
    user=Users.objects.get(id=i)
    user.delete()
    return redirect('/user', permanent=True)
def useredit(request,i):
    if(request.method=='POST'):
        A=Users.objects.get(id=i)
        A.id=request.POST['id']
        A.username=request.POST['username']
        A.firstname = request.POST['firstname']
        A.lastname = request.POST['lastname']
        A.persona = request.POST['persona']
        A.password = request.POST['password']
        A.save()
        return redirect('/user', permanent=True)
    user = Users.objects.get(id=i)
    return  render(request,'Users/useredit.html',{'user':user})