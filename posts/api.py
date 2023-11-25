# view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Posts
from .serializers import PostSerializer
@api_view(['GET'])
# دالة لتحويل البيانات الموجودة في جدول الى صيغة jason
def post_list_api(request):
    data1 = Posts.objects.all()
    data2 = PostSerializer(data1,many=True).data
    return Response({'data2':data2})

 