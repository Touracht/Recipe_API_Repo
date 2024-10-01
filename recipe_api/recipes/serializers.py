from rest_framework import serializers
from .models import Recipe, RateAndReview

class RecipeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Recipe model, handling creation and validation of recipe data.

    Fields:
        creator: The user who created the recipe.
        title: The title of the recipe.
        description: A brief description of the recipe.
        ingredients: The list of ingredients required for the recipe.
        instructions: Step-by-step instructions on how to prepare the recipe.
        category: The category of the recipe (e.g., dessert, main course).
        preparation_time: Time required to prepare the recipe in minutes.
        cooking_time: Time required to cook the recipe in minutes.
        servings: Number of servings the recipe yields.
        created_date: Timestamp of when the recipe was created (read-only).
        updated_date: Timestamp of when the recipe was last updated (read-only).
    """
    
    class Meta:
        model = Recipe
        fields = [
            'creator', 'title', 'description', 'ingredients', 
            'instructions', 'category', 'preparation_time', 
            'cooking_time', 'servings', 'created_date', 'updated_date'
        ]
        read_only_fields = ['created_date', 'updated_date']

    def validate_title(self, value):
        """
        Validate the title field.

        Args:
            value: The title of the recipe.

        Raises:
            serializers.ValidationError: If the title is empty.
        
        Returns:
            The validated title.
        """
        if not value:
            raise serializers.ValidationError('Title cannot be empty')
        return value
    
    def validate_ingredients(self, value):
        """
        Validate the ingredients field.

        Args:
            value: The list of ingredients for the recipe.

        Raises:
            serializers.ValidationError: If the ingredients list is empty.

        Returns:
            The validated ingredients list.
        """
        if not value:
            raise serializers.ValidationError('Ingredients must be provided')
        return value
        
    def validate_instructions(self, value):
        """
        Validate the instructions field.

        Args:
            value: The instructions for preparing the recipe.

        Raises:
            serializers.ValidationError: If the instructions are empty.

        Returns:
            The validated instructions.
        """
        if not value:
            raise serializers.ValidationError('Instructions must be provided')
        return value
        
    def validate_category(self, value):
        """
        Validate the category field.

        Args:
            value: The category of the recipe.

        Raises:
            serializers.ValidationError: If no category is chosen.

        Returns:
            The validated category.
        """
        if not value:
            raise serializers.ValidationError('Category must be chosen')
        return value
    
    def validate_preparation_time(self, value):
        """
        Validate the preparation time field.

        Args:
            value: The preparation time in minutes.

        Raises:
            serializers.ValidationError: If the time is negative.

        Returns:
            The validated preparation time.
        """
        if value < 0:
            raise serializers.ValidationError('Time field can only be positive')
        return value
        
    def validate_cooking_time(self, value):
        """
        Validate the cooking time field.

        Args:
            value: The cooking time in minutes.

        Raises:
            serializers.ValidationError: If the time is negative.

        Returns:
            The validated cooking time.
        """
        if value < 0:
            raise serializers.ValidationError('Time field can only be positive')
        return value
        
    def validate_servings(self, value):
        """
        Validate the servings field.

        Args:
            value: The number of servings.

        Raises:
            serializers.ValidationError: If servings are less than one.

        Returns:
            The validated number of servings.
        """
        if value < 1:
            raise serializers.ValidationError('Servings can only be one or more')
        return value

class RateAndReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for the RatingAndReview model, handling the creation of the RatingAndReview data.

    Fields: 
        user: the user who rated and reviewed the recipe.
        recipe: the recipe that is being rated and reviewed.
        review: a review message based on the recipe.
        rating: an out of 5 rating based on the recipe.
        created_date: Timestamp of when the review and/or rating were created (read-only).
        updated_date: Timestamp of when the review and/or rating were updated (read-only).
    """
    
    class Meta:
        model = RateAndReview
        fields = ['user', 'recipe', 'review', 'rating', 'created_date', 'updated_date']
        read_only_fields = ['created_date', 'updated_date']
