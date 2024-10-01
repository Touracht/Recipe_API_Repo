from django.shortcuts import render
from rest_framework import viewsets
from .models import Recipe, RateAndReview
from .serializers import RecipeSerializer, RateAndReviewSerializer
from rest_framework import permissions
from .paginations import RecipePagination, RateAndReviewPagination
from rest_framework.exceptions import PermissionDenied
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status

class RecipeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling Recipe-related CRUD operations.

    This viewset provides the ability to:
    - List all recipes (publicly accessible)
    - Retrieve a specific recipe (publicly accessible)
    - Create, update, or delete recipes (only for authenticated users)
    
    Additionally, it supports searching recipes based on various fields and filtering
    results based on cooking time, servings, or preparation time.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    pagination_class = RecipePagination

    def get_permissions(self):
        """
        Determine the permissions required for each action.

        - 'list' and 'retrieve' actions are publicly accessible.
        - All other actions (create, update, delete) require the user to be authenticated.
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        """
        Handle the creation of a new recipe.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"message": "Recipe created successfully!", "data": serializer.data}, 
                        status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        """
        Handle the update of an existing recipe.
        """
        instance = self.get_object()
        if instance.creator != request.user:
            raise PermissionDenied("You do not have permission to edit this recipe.")
        
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"message": "Recipe updated successfully!", "data": serializer.data},
                        status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        """
        Handle the deletion of a recipe.
        """
        instance = self.get_object()
        if instance.creator != request.user:
            raise PermissionDenied('You do not have permission to delete this recipe')
        
        self.perform_destroy(instance)
        return Response({"message": "Recipe deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        """
        Customize the queryset to support searching and filtering.
        """
        queryset = super().get_queryset()

        # Search functionality
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | 
                Q(category__icontains=search) | 
                Q(ingredients__icontains=search)
            )

        # Optional filters
        cooking_time = self.request.query_params.get('cooking_time', None)
        if cooking_time:
            queryset = queryset.filter(cooking_time__lte=cooking_time)

        servings = self.request.query_params.get('servings', None)
        if servings:
            queryset = queryset.filter(servings__gte=servings)

        preparation_time = self.request.query_params.get('preparation_time', None)
        if preparation_time:
            queryset = queryset.filter(preparation_time__lte=preparation_time)

        return queryset

class RateAndReviewViewSet(viewsets.ModelViewSet):
    queryset = RateAndReview.objects.all()
    serializer_class = RateAndReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = RateAndReviewPagination
    

