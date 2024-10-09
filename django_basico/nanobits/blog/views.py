from django.shortcuts import render

from blog.models import Post


def home(request):
    num_post = Post.objects.count()
    all_posts = Post.objects.all()
    return render(request, 'blog/home.html', {'num_posts': num_post, 'posts': all_posts})


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})
