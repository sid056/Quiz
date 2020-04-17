from django.shortcuts import render,redirect
from .forms import UserRegister,Registrationform

def Register(request) :
    if request.method == 'POST' :
        form1 = UserRegister(request.POST)
        
        form2 = Registrationform(request.POST)
        
        if form1.is_valid() and form2.is_valid() :
            
            x = form1.save()
            print (x)
            form2.save(x) 
            return redirect('/')
        else :
                
                print("FORM  OOMBI")

    else :

        form1 = UserRegister()
        form2 = Registrationform()


    return render(request,'reg.html',{'form1':form1 , 'form2':form2})    

