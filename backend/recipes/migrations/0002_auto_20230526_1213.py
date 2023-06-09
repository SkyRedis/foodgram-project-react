# Generated by Django 3.2 on 2023-05-26 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favourite',
            options={'ordering': ('user',), 'verbose_name': 'избранное', 'verbose_name_plural': 'избранные'},
        ),
        migrations.AlterModelOptions(
            name='ingredientrecipe',
            options={'ordering': ('-id',), 'verbose_name': 'IngredientRecipe'},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['name'], 'verbose_name': 'Рецепт', 'verbose_name_plural': 'Рецепты'},
        ),
        migrations.AlterModelOptions(
            name='shoppingcart',
            options={'ordering': ('user',), 'verbose_name': 'список покупок', 'verbose_name_plural': 'списки покупок'},
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to='backend_static/static/images/', verbose_name='изображение'),
        ),
    ]
