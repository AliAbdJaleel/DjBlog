# form
from rest_framework import serializers
from .models import Posts


class PostSerializer(serializers.ModelSerializer):

    # لاظهار قيم الحقول المرتبطة وليس الرقم
    auther = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    class Meta:
        model = Posts
        fields = '__all__'