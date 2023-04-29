from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Place(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pcode = models.CharField(max_length=10)
    pname = models.TextField()
    location = models.TextField()
    price = models.IntegerField(default=0)
    # 추가
    side = models.TextField()
    ball = models.TextField()
    vest = models.TextField()
    # 추가 항목(media)
    imgfile = models.ImageField(null=True, blank=True)
    modify_date = models.DateTimeField(null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.pcode + ' ' + self.pname + ' ' + self.location + ' ' + str(self.price)

class RentInfo(models.Model):
    pcode = models.CharField(max_length=10)
    pname = models.TextField()
    price = models.IntegerField(default=0)
    r_date = models.DateTimeField()

    def publish(self):
        self.p_date = timezone.now()
        self.save()

# Create your models here.
