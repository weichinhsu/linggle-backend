from django.shortcuts import render

def about(request):
    return render(request, 'about.html')

def news(request):
    return render(request, 'news.html')

def media(request):
    return render(request, 'media.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')