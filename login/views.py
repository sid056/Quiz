from django.shortcuts import render,redirect
from .forms import Login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from register.models import Userprofile

def Loginview(request) :
    if request.method == 'POST' :

        form = Login(request.POST)
        print(form)
        
        if form.is_valid() :
             username = form.cleaned_data['username']
             password = form.cleaned_data['password']
             
             
             user = authenticate(request , username=username , password=password)

             if user is not None :
                 
                login(request,user)
                return redirect('/home/')         

             else : 

                 return render(request , 'login.html' ,  {'val':'incorrect password or username' , 'form': form      } )
 

    else :
        
        form = Login()
        return render(request , 'login.html' , {'val':' ','form': form  } )

def Logoutview(request) :
    logout(request)
    form = Login()
    return redirect('/')

def online(request) :
    users = User.objects.all()
    return render(request , 'online.html' , {'users':users} )

    




