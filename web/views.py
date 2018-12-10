from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from rest_framework import mixins, viewsets

from back_web.models import Article, Item
from web.Serializer import ArticleSerializer, ItemSerializer


def index(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        articles = Article.objects.filter(open=0)
        paginator = Paginator(articles, 5)
        articles_page = paginator.page(page)
        return render(request, 'web/index.html', {'articles': articles_page})


def about(request):
    if request.method == 'GET':
        return render(request, 'web/about.html')


def list(request, id):
    if request.method == 'GET':
        if not id:
            page = int(request.GET.get('page', 1))
            articles = Article.objects.filter(open=0)
            paginator = Paginator(articles, 5)
            articles_page = paginator.page(page)
            return render(request, 'web/list.html', {'articles': articles_page,
                                                     'id': ''})
        else:
            page = int(request.GET.get('page', 1))
            item = Item.objects.filter(pk=id)
            articles = Article.objects.filter(open=0, item=item)
            paginator = Paginator(articles, 5)
            articles_page = paginator.page(page)
            return render(request, 'web/list.html', {'articles': articles_page,
                                                     'id': id})


class WebView(viewsets.GenericViewSet,
              mixins.ListModelMixin):
    queryset = Item.objects.all()

    serializer_class = ItemSerializer

    def get_queryset(self):
        item_type = []
        queryset = self.queryset
        for i in queryset:
            if i.article_set.count():
                item_type.append(i)
        return item_type


def look_art(request, id):
    if request.method == 'GET':
        if id:
            article = Article.objects.filter(pk=id).first()
            return render(request, 'web/info.html', {'article': article})
        else:
            return render(request, 'web/list.html')
