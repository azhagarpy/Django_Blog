from django.shortcuts import render
from .import models
# Create your views here.

def home(request):
    blogs=models.Blog.objects.all()
    comments=models.Comments.objects.all()
    data={'blogs':blogs,'comments':comments}
    return render(request,'Blog/index.html',{'data':data,'comments':comments})

