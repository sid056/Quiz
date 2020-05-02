from django.shortcuts import render
from save.models import data 
from django.db.models import Max
import random
import json

def quiz(request) :
    return render(request,'start.html')
