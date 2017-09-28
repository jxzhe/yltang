from django.shortcuts import render
from .models import Article, Comment

def article(request):
    itemList = []
    for article in Article.objects.all():
        items = [article]
        items.extend(list(Comment.objects.filter(article=article)))
        itemList.append(items)
    context = {'itemList': itemList}
    return render(request, 'article/article.html', context)