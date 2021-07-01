from django.shortcuts import render
from blog.models import Post, Comment

def blog_index(request):
    # ordered with the most recent post first.The minus sign tells Django to start with the largest value rather than the smallest. 
    post = Post.objects.all().order_by('-created_on')

    context = {
        'posts': posts
    }

    return render(request, 'blog_detail.html', context)

# Index posts from specific category chosen by the user
def blog_category(request, category):
    post = Post.objects.filter(categories__name__contains=category
    ).order_by('-created_on')
    
    context = {
        "category": category,
        "posts": posts
    }
    
    return render(request, "blog_category.html", context)

def blog_detail(request,pk):
    project = Blog.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }

    return render(request, "blog_detail.html", context)