from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    bio = models.TextField(blank=True)
    # Add any other fields you want for the user profile

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(blank=True, null=True)
    # Add any other fields you want for the blog post

    def __str__(self):
        return self.title

    def get_comment_count(self):
        return self.comments.count()

    def get_view_count(self):
        return self.views.count()


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    # Add any other fields you want for the comment
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.author.username} - {self.post.title}'


class Like(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_like = models.BooleanField(default=True)

    class Meta:
        unique_together = ['post', 'user']


class View(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='views')
    ip_address = models.GenericIPAddressField()
    session_id = models.CharField(max_length=100)

    class Meta:
        unique_together = ['post', 'session_id']


class Image(models.Model):
    image = models.ImageField(upload_to='blog_images')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    # Add any other fields you want for the image

    def __str__(self):
        return f'{self.owner.username} - {self.image.name}'
