from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
import datetime


class User(AbstractBaseUser):
    Name = models.CharField(max_length=40)
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(max_length=20)
    districtname = models.CharField(max_length=40)
    is_active = models.BooleanField(_('active'), default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ('Name', 'password', 'districtname')
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


    class Meta:
        db_table ="todo"

