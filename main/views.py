# main/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Follow 
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User  # Import User model
# Create your views here.


@login_required
def home(request):
    posts = Post.objects.all().order_by('-created_at')  # Fetch all posts, latest first
    users = User.objects.exclude(id=request.user.id)    # Exclude current user to avoid self-follow option

    return render(request, 'home.html', {
        'posts': posts,
        'users': users
    })
@login_required
def create_post(request):
    if request.method == 'POST':
        content = request.POST.get('content', '')  # Safely get the 'content' field
        if content:
            Post.objects.create(user=request.user, content=content)
        return redirect('home')
    return render(request, 'create_post.html')
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form, 'post': post})

@login_required
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    if user_to_follow != request.user:
        if user_to_follow.profile in request.user.profile.following.all():
            request.user.profile.following.remove(user_to_follow.profile)
        else:
            request.user.profile.following.add(user_to_follow.profile)
    return redirect('home')