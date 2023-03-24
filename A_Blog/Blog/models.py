from django.db import models
from datetime import datetime
import os
# Create your models here.

def imgsave(request,filename):
    old_filename=filename
    ctime=datetime.now()
    new_filename=f'{ctime}{old_filename}'
    return os.path.join('images/',new_filename)


class Category(models.Model):
    CategoryName=models.CharField(null=False,blank=False,max_length=40)
    CategoryImage=models.ImageField(upload_to=imgsave,blank=False,null=False)
    CategoryDate=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.CategoryName

class Blog(models.Model):
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    Title=models.CharField(max_length=150,blank=False)
    content=models.TextField(max_length=2000,blank=False)
    date=models.DateTimeField(auto_now_add=True)
    likes=models.IntegerField(blank=False)

    def __str__(self):
        return self.Title

class Comments(models.Model):
    blog_id=models.ForeignKey(Blog,on_delete=models.CASCADE)
    comments=models.CharField(max_length=200,blank=False)
    comment_accepted=models.BooleanField(default=False)

    def __str__(self):
        return str(self.blog_id)