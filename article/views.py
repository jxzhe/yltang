from django.shortcuts import render

def article(request):
    context = {}
    return render(request, 'article/article.html', context)