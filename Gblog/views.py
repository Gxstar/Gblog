from django.shortcuts import render


# Create your views here.


def show_home(request):
    return render(request, 'index.html', {'url': 'http://cdn.gxstar123.cn/jiuzhai-unsplash.jpg'})
