from django.contrib import admin
from .models import UserProfile, Category, BlogPost, Comment, Like, View, Image

# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class BlogPostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ('title', 'author', 'pub_date')
    list_filter = ('category', 'author')
    search_fields = ('title', 'author__username')


class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'is_like')
    list_filter = ('is_like',)


class ViewAdmin(admin.ModelAdmin):
    list_display = ('post', 'ip_address', 'session_id')
    search_fields = ('post__title', 'ip_address', 'session_id')


class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'owner', 'upload_date')
    search_fields = ('owner__username',)


admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment)
admin.site.register(Like, LikeAdmin)
admin.site.register(View, ViewAdmin)
admin.site.register(Image, ImageAdmin)
