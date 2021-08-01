from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid


# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email")

        if not username:
            raise ValueError("Users must have a username")

        token = uuid.uuid4()
        user = self.model(email=self.normalize_email(email), username=username, auth_token=token)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email=self.normalize_email(email), username=username, password=password)
        user.is_verified = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        print("Successfully created new superuser, ", user.username)
        return user


class Account(AbstractBaseUser):
    username = models.CharField(max_length=60, unique=True)
    email = models.EmailField(verbose_name="Email", max_length=60, unique=True)
    auth_token = models.CharField(max_length=100, blank=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = MyAccountManager()

    def __str__(self):
        token = str(self.auth_token)
        return token

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
