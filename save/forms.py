from django import forms

class questions(forms.Form) :
    quest = forms.CharField(widget=forms.Textarea, label="Question",max_length=200)
    option1 = forms.CharField(label="option1",max_length=50) 
    option2 = forms.CharField(label="option2",max_length=50) 
    option3 = forms.CharField(label="option3",max_length=50) 
    answer = forms.CharField(label="answer",max_length=50) 