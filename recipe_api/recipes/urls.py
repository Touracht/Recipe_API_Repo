from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, RateAndReviewViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'reviews', RateAndReviewViewSet)

urlpatterns = [
    path('', include(router.urls))
]
