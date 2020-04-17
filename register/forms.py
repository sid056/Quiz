from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Userprofile

class Registrationform(forms.ModelForm) :

    class Meta :
        model = Userprofile
        fields = (
            'city',
            # 'dob'
        )

    def save(self , x , commit=True) :

        user = User.objects.get(username=x)
        # city = self.cleaned_data['city']
        new = Userprofile.objects.get(user=user)
        new.city = self.cleaned_data['city']
        new.save()
        return new

    

class UserRegister(UserCreationForm) : 
    class Meta :
        model = User
        fields = (
            'username' ,
            'first_name',
            'last_name' ,
            'email',
            'password1' ,
            'password2' ,
        )
    def save(self , commit=True):
        user = super(UserRegister, self ).save(commit=False)
        user.first_name = self.cleaned_data['first_name'],
        user.last_name = self.cleaned_data['last_name'],        
        user.email = self.cleaned_data['email'],

        print(user)

        if commit :
            user.save()
        return user
