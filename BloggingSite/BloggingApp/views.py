from django.shortcuts import render,redirect

from .models import post



def index(request):
    p1 = post.objects.all()
    return render(request,'index.html',{"posts":p1})

# Create your views here.
