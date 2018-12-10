from rest_framework import serializers
from back_web.models import Admin


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        # 序列化模型
        model = Admin
        # 需要序列化的字段
        fields = ['id', 'username', 'name', 'tel']
