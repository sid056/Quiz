from django.shortcuts import render
from .forms import questions
from .models import data

def quizstart(request) :
    if request.method == 'POST' :
        q = questions(request.POST)

        if q.is_valid():
            print("thenks")
            quest = q.cleaned_data['quest']
            option1 = q.cleaned_data['option1']
            option2 = q.cleaned_data['option2']
            option3 = q.cleaned_data['option3']
            answer = q.cleaned_data['answer']

            new = data(question=quest,option1=option1,option2=option2,option3=option3,answer=answer)
            new.save()
            q = questions()
        else :
            print("form moonji")
            print(q)
    
    else:
         q = questions()

    return render(request,'forms.html',{'quest':q})

