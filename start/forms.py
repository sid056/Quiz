from django import forms 
from save.models import data
from django.db.models import Max
from random import randint

class start(forms.Form):
    f = True
    max_id = data.objects.aggregate(max_id=Max("id"))['max_id']
    while f :
        pk = randint(1,max_id)
        d = data.objects.get(pk=pk)
        
        if d :
            
            choice = [('choice1', d.option1),('choice2',d.option2),('choice3',d.option3)]
            question = forms.CharField(label=d.question)
            pk = forms.CharField(label=pk)
            c = forms.CharField(label=max_id)
            option = forms.ChoiceField(choices=choice, widget=forms.RadioSelect)
            f = False


    
    
    
     
