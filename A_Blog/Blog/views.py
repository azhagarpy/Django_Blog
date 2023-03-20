from django.shortcuts import render
from .import models


# Create your views here.

def home(request):
    blogs=models.Blog.objects.all()
    comments=models.Comments.objects.all()
    data={'blogs':blogs,'comments':comments}
    return render(request,'Blog/index.html',data)


def category(request):
    data=models.Category.objects.all()
    return render(request,'Blog/categorys.html',{'categorys':data})

def blog_category(request,cid):
    comments=models.Comments.objects.all()
    data=models.Blog.objects.filter(id=cid)
    return render(request,'Blog/blog_category.html',{'data':data,'comments':comments})