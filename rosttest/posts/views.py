from django.shortcuts import render
from .models import Post
# from main.models import Logo


# Представление для вывода постов
def posts_index(request):
    posts = Post.objects.order_by('-date_posted')
    return render(request, 'posts/posts_index.html', {'posts': posts})


def posts_macro(request):
    posts = Post.objects.order_by('-date_posted')
    return render(request, 'posts/macros/posts_macros.html', {'posts': posts})