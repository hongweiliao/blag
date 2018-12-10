from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from rest_framework import viewsets, mixins

from back_web.Serializer import AdminSerializer
from back_web.models import Admin, Article, Item
from back_web.ArtForm import AddArtForm, AddItemForm


def index(request):
    if request.method == 'GET':
        return render(request, 'backweb/index.html')


def article(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        articles = Article.objects.all()
        paginator = Paginator(articles, 7)
        articles_page = paginator.page(page)
        return render(request, 'backweb/article.html', {'articles': articles_page})


def category(request):
    page = int(request.GET.get('page', 1))
    items = Item.objects.all()
    paginator = Paginator(items, 20)
    item_page = paginator.page(page)
    if request.method == 'GET':
        return render(request, 'backweb/category.html', {'items': item_page})
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            # 表示验证成功
            name = form.cleaned_data['name']
            asname = form.cleaned_data['alias']
            father_id = request.POST.get('fid')
            item = Item.objects.filter(pk=father_id).first()
            describe = form.cleaned_data['describe']
            if item:
                Item.objects.create(name=name, asname=asname, father=item, desc=describe)
            else:
                Item.objects.create(name=name, asname=asname, desc=describe)
            return HttpResponseRedirect(reverse('admin:cate'))
        else:
            # 表示验证失败需要将错误信息给页面展示
            return render(request, 'backweb/add-article.html', {'form': form.errors,
                                                                'items': item_page})


def add_article(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        items = Item.objects.all()
        paginator = Paginator(items, 20)
        item_page = paginator.page(page)
        return render(request, 'backweb/add-article.html', {'items': item_page})
    if request.method == 'POST':
        form = AddArtForm(request.POST)
        if form.is_valid():
            # 表示验证成功
            item = Item.objects.filter(pk=request.POST.get('category')).first()
            Article.objects.create(title=form.cleaned_data.get('title'), desc=form.cleaned_data.get('desc'),
                                   content=form.cleaned_data.get('content'), state='发布', item=item,
                                   open=request.POST.get('visibility'))
            return HttpResponseRedirect(reverse('admin:art'))
        else:
            # 表示验证失败需要将错误信息给页面展示
            return render(request, 'backweb/add-article.html', {'form': form.errors})


def login(request):
    if request.method == 'GET':
        return render(request, 'backweb/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('userpwd')
        admin = Admin.objects.filter(username=username).first()
        if admin:
            if password == admin.password:
                request.session['user_id'] = admin.id
                res = HttpResponseRedirect(reverse('admin:index'))
                return res
            else:
                message = '密码不正确'
        else:
            message = '用户名不存在'
        return JsonResponse({'message': message}, json_dumps_params={'ensure_ascii': False})


def delete_art(request, id):
    if request.method == 'GET':
        Article.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('admin:art'))


def update_art(request, id):
    page = int(request.GET.get('page', 1))
    items = Item.objects.all()
    paginator = Paginator(items, 20)
    item_page = paginator.page(page)
    article = Article.objects.filter(pk=id).first()
    if request.method == 'GET':
        return render(request, 'backweb/update-article.html', {'items': item_page, 'article': article})
    if request.method == 'POST':
        form = AddArtForm(request.POST)
        if form.is_valid():
            # 表示验证成功
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            desc = form.cleaned_data['desc']
            item = Item.objects.filter(pk=request.POST.get('category')).first()
            open = request.POST.get('visibility')
            article.title = title
            article.content = content
            article.desc = desc
            article.item = item
            article.open = open
            article.save()
            return HttpResponseRedirect(reverse('admin:art'))

        else:
            # 表示验证失败需要将错误信息给页面展示
            return render(request, 'backweb/update-article.html', {'form': form.errors, 'article': article,
                                                                   'items': item_page})


def update_cat(request, id):
    items = Item.objects.all()
    item = Item.objects.filter(pk=id).first()
    if request.method == 'GET':
        return render(request, 'backweb/update-category.html', {'items': items,
                                                                'now_item': item})
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            item.name = form.cleaned_data['name']
            item.asname = form.cleaned_data['alias']
            item.desc = form.cleaned_data['describe']
            father_id = request.POST.get('fid')
            if father_id == '0':
                item.father_id = ''
            else:
                item.father_id = father_id
            item.save()
            return HttpResponseRedirect(reverse('admin:cate'))
        else:
            return render(request, 'backweb/update-category.html', {'items': items,
                                                                    'now_item': item})


def delete_cat(request, id):
    if request.method == "GET":
        Item.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('admin:cate'))


def logout(request):
    del request.session['user_id']
    return HttpResponseRedirect(reverse('admin:login'))


def manage_user(request):
    if request.method == "GET":
        return render(request, 'backweb/manage-user.html')
    if request.method == "POST":
        return render(request, 'backweb/manage-user.html')


class User(viewsets.GenericViewSet,
           mixins.ListModelMixin,
           mixins.CreateModelMixin):
    queryset = Admin.objects.all()

    serializer_class = AdminSerializer

    def create(self, request, *args, **kwargs):
        pass
