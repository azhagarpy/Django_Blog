from django.shortcuts import render,redirect
from django.contrib import messages
from .import models


# Create your views here.



def home(request):
    blogs=models.Blog.objects.filter(likes__gt=100)
    comments=models.Comments.objects.all()
    data={'blogs':blogs,'comments':comments}
    return render(request,'Blog/index.html',data)


def category(request):
    data=models.Category.objects.all()
    return render(request,'Blog/categorys.html',{'categorys':data})

def blog_category(request,cid):
    comments=models.Comments.objects.all()
    data=models.Blog.objects.filter(category_id=cid)
    return render(request,'Blog/blog_category.html',{'data':data,'comments':comments})

def add_comment(request,cid):
    a=models.Blog.objects.get(id=cid)
    comment=request.POST.get('comment')
    models.Comments.objects.create(blog_id=a,comments=comment)
    messages.success(request,'Comment Added Success')
    return redirect('home')


def add_like(request,blog_id):
    obj=models.Blog.objects.get(id=blog_id)
    obj.likes+=1
    obj.save()
    messages.success(request,'Like Added Success')
    print(request.path)
    return redirect('home')