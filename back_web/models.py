from django.db import models


# Create your models here.
class Admin(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=50, default='未命名')
    tel = models.CharField(max_length=11, default='')

    class Meta:
        db_table = 'user'


class Item(models.Model):
    name = models.CharField(max_length=50)
    asname = models.CharField(max_length=20)
    father = models.ForeignKey('self', null=True)
    desc = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'item'


class Article(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    content = models.TextField()
    state = models.CharField(max_length=10)
    create_time = models.DateTimeField(auto_now_add=True)
    open = models.CharField(max_length=10, null=True)
    item = models.ForeignKey(Item, null=True)

    class Meta:
        db_table = 'article'










