from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'        

# Create your models here.
class Blog(models.Model):
    STATUS_BLOG=(
        ('draft',"Draft"),
        ('published',"Published"),
    )
    user=models.ForeignKey(User,on_delete=None)
    category = models.ForeignKey(Category,on_delete=None)
    title=models.CharField(max_length=255)
    seo_text=models.CharField(max_length=255,default='',blank=True)
    slug=models.SlugField(max_length=255)
    content=models.TextField()
    status=models.CharField(max_length=10, choices=STATUS_BLOG, default='draft')
    published_at=models.DateTimeField(default=timezone.now)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog=models.ForeignKey(Blog,on_delete=None,related_name="comments")
    user=models.ForeignKey(User,on_delete=None)
    comment=models.TextField()

    created_at=models.DateTimeField(auto_now_add=True)
    approved=models.BooleanField(default=False)
    anonymous=models.BooleanField(default=False)

    def __str__(self):
        return self.comment+"-"+str(self.created_at) 