from django.db import models

class Icalc(models.Model):
    principle = models.CharField(max_length=100)
    rate = models.CharField('interest Rate' ,max_length=100)
    initial_time = models.DateField('सापटि लगेको समय')
    final_time = models.DateField('पैशा बुजाएको समय')
