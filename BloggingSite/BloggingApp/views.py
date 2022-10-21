from django.shortcuts import render,redirect

from .models import post

# Create your views here.
def index(request):
    p1 = post.objects.all()
    return render(request,'index.html',{"posts":p1})

def posts(request,pk):
    p1 =post.objects.get(id=pk)
    return render(request,'posts.html',{'pk':p1})
    