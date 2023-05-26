from django.contrib.auth.models import AbstractUser
from django.db import models


class UserFoodgram(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'first_name', 'last_name')
    email = models.EmailField(
        'Email адрес', max_length=254, unique=True)
    username = models.CharField(
        'Уникальный юзернейм', max_length=150, unique=True)
    first_name = models.CharField('Имя', max_length=150, blank=True)
    last_name = models.CharField('Фамилия', max_length=150, blank=True)
    password = models.CharField('Пароль', max_length=150)

    class Meta:
        ordering = ['username', ]
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return self.username


class Subscribe(models.Model):
    user = models.ForeignKey(
        UserFoodgram, on_delete=models.CASCADE,
        related_name='subscriber',
        verbose_name='Пользователь')
    author = models.ForeignKey(
        UserFoodgram, on_delete=models.CASCADE,
        related_name='subscribing',
        verbose_name='Автор')

    class Meta:
        ordering = ['author', ]
        verbose_name = 'Подписка на автора'
        verbose_name_plural = 'Подписки на авторов'
        constraints = [models.UniqueConstraint(
            fields=['user', 'author'],
            name='unique_follow')]

    def __str__(self) -> str:
        return (
            f'Пользователь {self.user}'
            f' подписался на {self.author.username}')
