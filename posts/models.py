from django.db import models
from taggit.managers import TaggableManager
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
'''




'''


class Posts(models.Model):
    auther = models.ForeignKey(User,related_name='post_auther',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=20000)
    draft = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='post')
    category = models.ForeignKey('Category',related_name='post_category',on_delete=models.SET_NULL,null=True)
    #file = models.FileField()
   # publish_date2 = models.DateTimeField(auto_now= True) # يتم انشاء عمود ياخذ تاريخ و وقت ادراج القيد دون ان يظهر للمستخدم
   # publish_date3 = models.DateTimeField(auto_now_add= True) # يتم انشاء عمود ياخذ تاريخ و وقت تحديث القيد دون ان يظهر للمستخدم

    tags = TaggableManager()

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

class Comment(models.Model):
    post = models.ForeignKey(Posts,related_name='comment_post',on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    comment = models.TextField(max_length=300)
    created_at = models.DateTimeField(timezone.now)
    
    def __str__(self):
        return str(self.post)

