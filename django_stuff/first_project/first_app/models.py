from django.db import models

# Create your models here.


class Topic(models.Model):
    topic_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.topic_name
    
class Webpage(models.Model):
    topic_name = models.ForeignKey(Topic, on_delete = models.SET_NULL, null=True)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name
    
class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete = models.SET_NULL, null=True, default='free')
    date = models.DateField()

    def __str__(self):
        return str(self.date)

    