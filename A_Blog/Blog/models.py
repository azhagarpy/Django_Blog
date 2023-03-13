from django.db import models
from datetime import datetime
# Create your models here.


class Blog(models.Model):
    Title=models.CharField(max_length=150,blank=False)
    content=models.TextField(max_length=2000,blank=False)
    date=models.DateTimeField(auto_now_add=True)
    Category=models.CharField(max_length=100,blank=False)
    likes=models.IntegerField(blank=False)

    def __str__(self):
        return self.Title

class Comments(models.Model):
    c=models.ForeignKey(Blog,on_delete=models.CASCADE)
    comments=models.CharField(max_length=200,blank=False)

    def __str__(self):
        return self.comments