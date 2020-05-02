import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async

from save.models import data 
from django.db.models import Max
import random

class QuizConsumer(AsyncConsumer) :
    async def websocket_connect(self,event):
        print("Connected")
        max_id = await self.get_max_id()
        lst = list(range(max_id))
        shfl = random.sample(lst , max_id)
        print(shfl)
        datas = await self.get_data()
        response = {
            "list" : shfl ,
            "data" : datas
        }
        await self.send({
            "type":"websocket.accept",
        })
        await self.send({
            "type" : "websocket.send" ,
            "text" : json.dumps(response)
        })


    async def websocket_receive(self,event):
        print("Recieved",json.loads(event['text']))
        response = json.loads(event['text'])
        await self.send({
            "type" : "websocket.send" ,
            "text" : json.dumps(response),
        })

    async def websocket_disconnect(self,event):
        print("Disconnected")
    
    @database_sync_to_async
    def get_data(self) :
        db = data.objects.all()
        question = []
        i = 0
        questiondict = {}
        for quiz in db : 
            questiondict[i] = {}
            questiondict[i]['question'] = quiz.question
            questiondict[i]['options'] = [quiz.option1,quiz.option2,quiz.option3]
            questiondict[i]['answer'] = quiz.answer
            i = i+1
        return questiondict

    @database_sync_to_async
    def get_max_id(self) :
        max_id = data.objects.aggregate(max_id=Max("id"))['max_id']
        return max_id