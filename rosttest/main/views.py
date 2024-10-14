from django.shortcuts import render
# from .models import Logo
from posts.models import Post

# Create your views here.
from django.http import HttpResponse



def index(request):
    posts = Post.objects.order_by('-date_posted')
    # logo = Logo.objects.last()  # Получаем последний загруженный логотип
    return render(request, 'main/index.html', {'posts': posts})

def about(request):
    # return HttpResponse("Hello World about")
    return render(request, 'main/about.html')

# def logo_image(request):
#     logo = Logo.objects.last()  # Получаем последний загруженный логотип
#     return render(request, 'main/base/layout.html', {'logo': logo})