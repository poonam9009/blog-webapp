from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class BlogAppPost(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=332, default="")
    author = models.CharField(default="",max_length=354)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=8000,default="")
    slug = models.CharField(max_length = 324,default="")
    # views = models.IntegerField(default=0)
    thumbnail = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.title + " by " + self.author

class Comments(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.CharField(max_length =500,default="")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(BlogAppPost,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null = True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:10] + "..." + " by "+ self.user.email
    