# form
from rest_framework import serializers
from django.contrib.auth.models import User # لغرض عرض تفاصيل المستخدم الذي قام بتحديث القيد او ادراجه
from .models import Posts


# هذه الكلاس لاظهار تفاصيل المستخدم او المؤلف في الجدول الرئيسي
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']




class PostSerializer(serializers.ModelSerializer):

    # لاظهار قيم الحقول المرتبطة وليس الرقم
    auther = UserSerializer()
    category = serializers.StringRelatedField()
    class Meta:
        model = Posts
        fields = '__all__'