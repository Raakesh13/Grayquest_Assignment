from django.db import models
from django.contrib.auth.models import User


class Cookies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    setCookies = models.BooleanField(default=False)
