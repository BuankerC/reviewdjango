from django.db import models
from django.core.validators import EmailValidator
from django.conf import settings
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, validators=[EmailValidator])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL) 