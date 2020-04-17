from django.shortcuts import render
from save.models import data 
from django.db.models import Max
import random

def quiz(request) :
    max_id = data.objects.aggregate(max_id=Max("id"))['max_id']
    lst = list(range(10))
    shfl = random.shuffle(lst)
    db = data.objects.all()
    return render(request,'start.html',{'lst':shfl , 'db':db})

