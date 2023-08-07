from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost, Comment, Like, View
from .forms import CommentForm


def home(request):
    # Assuming you want to display the latest blog posts on the homepage
    latest_posts = BlogPost.objects.order_by('-pub_date')
    context = {
        'latest_posts': latest_posts,
    }
    return render(request, 'home.html', context)


def blog_post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)

    # Record view for the post
    ip_address = request.META.get('REMOTE_ADDR')  # Get the IP address from the request
    session_id = request.session.session_key
    View.objects.get_or_create(post=post, ip_address=ip_address, session_id=session_id)

    comments = Comment.objects.filter(post=post, parent_comment=None)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('blog_post_detail', pk=pk)
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'blog_post_detail.html', context)

@login_required
def like_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    user = request.user

    if request.method == 'POST':
        like_type = request.POST.get('like_type')

        if like_type == 'like':
            Like.objects.get_or_create(post=post, user=user, is_like=True)
        elif like_type == 'dislike':
            Like.objects.get_or_create(post=post, user=user, is_like=False)

    return redirect('blog_post_detail', pk=pk)
