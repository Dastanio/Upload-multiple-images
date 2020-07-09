from django.shortcuts import render, get_object_or_404

from .models import PostImage, Post

def blog_view(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'blog.html', context)

def detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    photos = PostImage.objects.filter(post=post)
    context = {
        'post':post,
        'photos':photos
    }
    return render(request, 'detail.html', context)

