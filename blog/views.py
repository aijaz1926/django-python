from django.shortcuts import render
from django.http import HttpResponse

from .models import Blog,Comment,Category

# Create your views here.
def get_all_blog(request):
    blogs = Blog.objects.all()
    categories = Category.objects.all()
    template_url = 'blog/posts/all_blog.html'
    context = {
        'blogs': blogs,
        'categories':categories,
        'user':request.user
    }
    return render(request, template_url, context)

def get_blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    template_url = 'blog/posts/blog.html'
    context = {
        'blog': blog
    }
    return render(request, template_url, context)
