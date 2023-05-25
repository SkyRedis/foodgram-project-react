from django.urls import include, path
from rest_framework import routers

from .views import IngredientViewSet, RecipeViewSet, TagViewSet, UsersViewSet

app_name = 'api'

router_api = routers.DefaultRouter()

router_api.register('users', UsersViewSet, basename='users')
router_api.register('ingredients', IngredientViewSet, basename='ingredients')
router_api.register('recipes', RecipeViewSet, basename='recipes')
router_api.register('tags', TagViewSet, basename='tags')

urlpatterns = [
    path('', include(router_api.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
