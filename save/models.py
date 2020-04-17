from django.db import models


class data(models.Model) :
    question = models.TextField()
    option1 = models.TextField()
    option2 = models.TextField()
    option3 = models.TextField()
    answer = models.TextField()
 