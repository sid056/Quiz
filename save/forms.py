from django import forms

class questions(forms.Form) :
    quest = forms.CharField(widget=forms.Textarea(
        attrs = {"class":"form-control z-depth-1 textarea-extra " , "id":"exampleFormControlTextarea6" ,
        "rows":"3" , "placeholder":"Write something here..."}
    ), label="Question",max_length=200)
    option1 = forms.CharField(label="option1",max_length=50) 
    option2 = forms.CharField(label="option2",max_length=50) 
    option3 = forms.CharField(label="option3",max_length=50) 
    answer = forms.CharField(label="answer",max_length=50) 