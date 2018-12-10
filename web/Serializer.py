from rest_framework import serializers
from back_web.models import Article, Item


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        # 序列化模型
        model = Article
        # 需要序列化的字段
        fields = ['item_id']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        # 序列化模型
        model = Item
        # 需要序列化的字段
        fields = ['id', 'name']



