from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
import datetime


class User(AbstractBaseUser):
    Name = models.CharField(max_length=40)
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(max_length=20)
    is_active = models.BooleanField(_('active'), default=True)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)

    REQUIRED_FIELDS = ('Name', 'password')
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'tododemo'


class Todolist(models.Model):
    taskname = models.CharField(max_length=120)
    status = models.CharField(max_length=120, default='active')

    def _str_(self):
        return self.taskname

