from dataclasses import Field
from email.policy import default
from enum import unique
from random import choice

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):

        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name

        )

        user.set_password(password)
        user.save(using=self.db)

        return user



    def create_superuser(self, first_name, last_name, username, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name


        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True

        user.save(using=self._db)
        return user


class User(AbstractUser):
    RESTAURANT = 1
    CUSTOMER = 2
    ROLE_EHOICE = (
        (RESTAURANT, 'Restaurant'),
        (CUSTOMER, 'Customer')

    )


    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True,max_length=100)
    role = models.PositiveSmallIntegerField(choices=ROLE_EHOICE, blank=True, null = True)



    data_joined = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)
    created_data = models.DateTimeField(auto_now=True)
    modified_data = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)


USERNAME_FIELD = 'email'
REQUIRED_FIELD = ['username', 'first_name','last_name', ]
objects = UserManager()

def __str__(self):
    return self.email


def has_perm(self, perm, obj=None):
    return self.is_admin

def has_module_perm(self,applabel):
    return True









