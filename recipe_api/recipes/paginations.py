from rest_framework.pagination import PageNumberPagination

class RecipePagination(PageNumberPagination):
    page_size = 20

class RateAndReviewPagination(PageNumberPagination):
    page_size = 30

class FollowingFeedPagination(PageNumberPagination):
    page_size = 20

class FavoriteFeedPagination(PageNumberPagination):
    page_size = 20