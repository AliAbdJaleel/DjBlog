# view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Posts
from .serializers import PostSerializer


#function based

""" @api_view(['GET'])
# دالة لتحويل البيانات الموجودة في جدول الى صيغة jason
def post_list_api(request):
    data1 = Posts.objects.all()
    data2 = PostSerializer(data1,many=True).data
    return Response({'data2':data2})


@api_view(['GET','DELETE','POST']) 
def post_detail_api(request,id):
    data1 = Posts.objects.get(id=id)
    data2 = PostSerializer(data1).data
    return Response({'data2':data2})
 """



#CBV

from rest_framework import generics

""" class PostListAPI(generics.ListAPIView): # هذه الكلاس لاستعراض جميع القيود الموجودة في قاعدة البيانات
    queryset =  Posts.objects.all()
    serializer_class = PostSerializer """


""" class PostDetailAPI(generics.RetrieveAPIView):  # هذه الكلاس فقط لاستعراض القيد
    queryset = Posts.objects.all()
    serializer_class = PostSerializer """


    

class PostDetailAPI(generics.RetrieveUpdateDestroyAPIView): # هذه الكلاس لاستعراض البيانات و تعديلها و حذفها
    queryset = Posts.objects.all()
    serializer_class = PostSerializer




class PostListAPI(generics.ListCreateAPIView):    # هذه الكلاس لاستعراض القيود الموجودة في قاعدة البيانات و الاضافة عليها
    queryset =  Posts.objects.all()
    serializer_class = PostSerializer
