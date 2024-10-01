from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, RateAndReviewViewSet, AddToFavoritesView, RemoveFromFavoritesView

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'reviews', RateAndReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/favorite/', AddToFavoritesView.as_view(), name='favourite'),
    path('<int:pk>/undo favorite/', AddToFavoritesView.as_view(), name='undo favourite'),
]
