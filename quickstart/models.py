import uuid
import os
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('images/products', filename)


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Создан в ")
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен в ')

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Product(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Название ')
    price = models.IntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name="Описание ")
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True, verbose_name="Изображение ")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', null=True, verbose_name="Категория ")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = 'Products'


class UserManager(BaseUserManager):

    use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self.create_user(email, password, **extra_fields)


class UserData(AbstractUser):
    username = None
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name


class WishList(BaseModel):
    user = models.ForeignKey(UserData, on_delete=models.CASCADE, related_name='wishlists')
    product = models.ManyToManyField(Product, related_name='wishlists')

    def __str__(self) -> str:
        return self.user.name + " wishlist"

    class Meta:
        verbose_name_plural = 'WishLists'


class Cart(BaseModel):
    user = models.ForeignKey(UserData, on_delete=models.CASCADE, related_name='cart')
    product = models.ManyToManyField(Product, related_name='cart')

    def __str__(self) -> str:
        return self.user.name + " cart"

    class Meta:
        verbose_name_plural = 'Cart'
