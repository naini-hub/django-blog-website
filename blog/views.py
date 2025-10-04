from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


posts = [
    {
        'author':'Gaurav nainwal',
        'title':'blog post 1',
        'content':'first blog post content',
        'date_posted':'August 28, 2025'
    },
    {
        'author':'John doe',
        'title':'blog post 2',
        'content':'second blog post content',
        'date_posted':'August 29, 2025'
    }

]

def home(request):

    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'about'})