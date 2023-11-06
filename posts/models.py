from django.db import models
from taggit.managers import TaggableManager
from django.utils import timezone
# Create your models here.
'''




'''


class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=20000)
    draft = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=timezone.now)
   # publish_date2 = models.DateTimeField(auto_now= True) # يتم انشاء عمود ياخذ تاريخ و وقت ادراج القيد دون ان يظهر للمستخدم
   # publish_date3 = models.DateTimeField(auto_now_add= True) # يتم انشاء عمود ياخذ تاريخ و وقت تحديث القيد دون ان يظهر للمستخدم

    tags = TaggableManager()

    def __str__(self):
        return self.titleS