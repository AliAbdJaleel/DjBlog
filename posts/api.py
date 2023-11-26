# view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Posts
from .serializers import PostSerializer


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



from rest_framework import generics
class PostListAPI(generics.ListAPIView):
    queryset =  Posts.objects.all()
    serializer_class = PostSerializer


class PostDetailAPI(generics.RetrieveAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer