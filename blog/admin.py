from django.contrib import admin

from . import models

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', )
    

class BlogAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('category','title', 'slug', 'content', 'status','blog_user','seo_text')
    search_fields = ('content', 'title')
    prepopulated_fields = {'slug': ('title',)}    

    def blog_user(self, obj):
        return obj.user.username+"("+obj.user.email+")"

    def seo_text(self,obj):
        return obj.seo_text

    seo_text.empty_value_display='NOT_PROVIDED'


admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.Blog, BlogAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment','approved','anonymous','user')

    def user(self, obj):
        return obj.user.username

admin.site.register(models.Comment, CommentAdmin);    

# Register your models here.
