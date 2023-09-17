from django.contrib.auth.models import AbstractUser
from django.db import models

ADMINISTRATOR = 'Administrator'
COMPANY = "Company"
STORE_OWNER = 'Store Owner'
STORE_MANAGER = 'Store Manager'

ROLE_CHOICES = [
    (ADMINISTRATOR, 'Administrator'),
    (COMPANY, "Company"),
    (STORE_OWNER, 'Store Owner'),
    (STORE_MANAGER, 'Store Manager'),
]

class User(AbstractUser):

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=150)
    role = models.CharField(choices=ROLE_CHOICES, default=ROLE_CHOICES[2], max_length=150)



    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_users',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_users',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username

class Company(User):
    adress = models.CharField(max_length=150)
    tin = models.CharField(max_length=255)
    FOOD = "Food"
    HAUSEHOLD = "Hausehold"

    TYPE_PRODUCTS = [
        (FOOD, "Food"),
        (HAUSEHOLD, "Hausehold")
    ]
    type_products = models.CharField(max_length=20, choices=TYPE_PRODUCTS)

class Store_Owner(User):
    tin = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)

