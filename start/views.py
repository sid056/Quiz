from django.shortcuts import render
from save.models import data 
from django.db.models import Max
import random
import json

def quiz(request) :
    max_id = data.objects.aggregate(max_id=Max("id"))['max_id']
    lst = list(range(max_id))
    shfl = random.shuffle(lst)
    db = data.objects.all()
    question = []
    i = 0
    questiondict = {}
    for quiz in db : 
        questiondict[quiz.question] = {}
        questiondict[quiz.question]['id'] = i
        questiondict[quiz.question]['options'] = [quiz.option1,quiz.option2,quiz.option3]
        questiondict[quiz.question]['answer'] = quiz.answer
        i = i+1

    questiondict = json.dumps(questiondict)
    print(questiondict)

    return render(request,'start.html',{'lst':lst , 'db':questiondict})
