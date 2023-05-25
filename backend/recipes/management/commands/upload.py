from csv import DictReader

from django.core.management.base import BaseCommand

from recipes.models import Ingredient, Tag


def load_ingredients():
    print('loading ingredient data...')
    with open('data/ingredients.csv', encoding='utf-8') as file:
        reader = DictReader(file)
        ingredients = []
        for row in reader:
            ingredient = Ingredient(
                id=row['id'],
                name=row['name'],
                measurement_unit=row['measurement_unit']
            )
            ingredients.append(ingredient)
        Ingredient.objects.bulk_create(ingredients)
    print('ingredients data loaded!')


def load_tags():
    print('loading tag data...')
    with open('data/tags.csv', encoding='utf-8') as file:
        reader = DictReader(file)
        tags = []
        for row in reader:
            tag = Tag(
                id=row['id'],
                name=row['name'],
                color=row['color'],
                slug=row['slug']
            )
            tags.append(tag)
        Tag.objects.bulk_create(tags)
    print('Tags data loaded!')


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            load_ingredients()
            load_tags()
        except Exception as error:
            print(error)
