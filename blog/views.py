from django.shortcuts import render
from blog.models import Post, Comment
from .forms import CommentForm


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
        "posts": posts,
    }

    return render(request, "blog_category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    # if a POST request has been received. Then we create a new instance of our form
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)

        # is_valid() checks that all the fields have been entered correctly.
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog_detail.html", context)
