from django.shortcuts import render,get_object_or_404,reverse
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseForbidden
from .forms import CommentForm
from .models import Blog,Comment,Category
from django.contrib.auth.decorators import login_required

# Create your views here.
def get_all_blog(request):
    blogs = Blog.objects.filter(status='published')
    categories = Category.objects.all()
    template_url = 'blog/blog/all_blog.html'
    context = {
        'blogs': blogs,
        'categories':categories,
        'user':request.user
    }
    return render(request, template_url, context)

@login_required
def get_blog(request, slug):
    blog = get_object_or_404(Blog,slug=slug)
    categories = Category.objects.all()
    template_url = 'blog/blog/blog.html'
    context = {
        'categories':categories,
        'blog': blog,
        'comments':blog.comments.order_by('-created_at')
    }
    return render(request, template_url, context)

def get_blog_by_category(request, category):
    oCategory = get_object_or_404(Category,name=category)
    blogs = Blog.objects.filter(category=oCategory)
    categories = Category.objects.all()
    template_url = 'blog/category/blogs.html'
    context = {
        'blogs': blogs,
        'categories':categories,
        'user':request.user,
        'category':category
    }
    return render(request, template_url, context)
   
def add_comment(request, blog_slug):
    user  = request.user
    if not user.has_perm('blog.add_comment'):
        return HttpResponseForbidden()

    blog = get_object_or_404(Blog, slug=blog_slug)

    if(request.method == 'POST'):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('blog:get_blog', args=[blog_slug]))
    else:
        form = CommentForm()
    
    return render(request, 'blog/comment/post_comment.html', {
        'form':form,
        'blog':blog
    })