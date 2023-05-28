from django.conf import settings as s
from django.core.validators import MinValueValidator
from django.db import models
from users.models import UserFoodgram

User = UserFoodgram


class Ingredient(models.Model):
    name = models.CharField(
        'Наименование', max_length=200, db_index=True)
    measurement_unit = models.CharField(
        'единица измерения', max_length=200, default='кг')

    class Meta:
        ordering = ['name', ]
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField('название', unique=True, max_length=200)
    color = models.CharField('цвет в HEX', unique=True, max_length=7)
    slug = models.SlugField('уникальный слаг', unique=True, max_length=200)

    class Meta:
        ordering = ['name', ]
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self) -> str:
        return self.name


class Recipe(models.Model):
    name = models.CharField(
        'Наименование', max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='автор рецепта')
    ingredients = models.ManyToManyField(
        Ingredient, related_name='recipes',
        verbose_name='ингредиенты',
        help_text='Добавьте ингредиент',
        through='IngredientRecipe')
    tags = models.ManyToManyField(
        Tag, related_name='recipes',
        verbose_name='теги')
    image = models.ImageField(
        'изображение', upload_to='backend_static/static/images/')
    text = models.TextField(
        'описание рецепта',
        help_text='Добавьте описание рецепта!')
    cooking_time = models.PositiveSmallIntegerField(
        'время приготовления(мин.)',
        validators=[MinValueValidator(
            s.CONST_NUMBER_ONE, message='Минимум 1 минута!')])
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации рецепта',
        auto_now_add=True,
    )

    class Meta:
        ordering = ['-pub_date', ]
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self) -> str:
        return self.name


class IngredientRecipe(models.Model):
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE,
        related_name='ingredient_recipe', verbose_name='ингредиент')
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        related_name='ingredient_recipe', verbose_name='рецепт')
    amount = models.PositiveSmallIntegerField(
        'вес', validators=[MinValueValidator(
            s.CONST_NUMBER_ONE, message='Значение менее 1')])

    class Meta:
        ordering = ('-id', )
        verbose_name = 'IngredientRecipe'

    def __str__(self) -> str:
        return (
            f'{self.ingredient.name} - {self.amount}'
            f'{self.ingredient.measurement_unit}')


class Favourite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favourites',
        verbose_name='пользователь',)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favourites',
        verbose_name='рецепт',)

    class Meta:
        ordering = ('user', )
        verbose_name = 'избранное'
        verbose_name_plural = 'избранные'
        constraints = [
            models.UniqueConstraint(fields=['user', 'recipe'],
                                    name='unique_favourite')]

    def __str__(self):
        return f'Пользователь {self.user} добавил {self.recipe} в избранное'


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='пользователь')
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='рецепт')

    class Meta:
        ordering = ('user', )
        verbose_name = 'список покупок'
        verbose_name_plural = 'списки покупок'
        constraints = [models.UniqueConstraint(
            fields=['user', 'recipe'], name='unique_shopping_cart')]

    def __str__(self):
        return (
            f'Пользователь {self.user}'
            f' добавил в список покупок {self.recipe.name}')
