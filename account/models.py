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
    # User is Store Shop or Mall MANAGER who orders goods

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


class Producer(User):
    address = models.CharField(max_length=150)
    tin = models.CharField(max_length=255)
    FOOD = "Food"
    HOUSEHOLD = "Household"

    TYPE_PRODUCTS = [
        (FOOD, "Food"),
        (HOUSEHOLD, "Household")
    ]
    type_products = models.CharField(max_length=20, choices=TYPE_PRODUCTS)


class StoreOwner(User):
    # just owns a store, can't order but can see orders
    tin = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)


