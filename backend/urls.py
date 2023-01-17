from django.urls import path,include
# from .views import article_list, article_details
# from .views import ArticleList, ArticleDetails
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter
# ROUTER VIEW START
router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
# ROUTER VIEW ENDS HERE
urlpatterns = [
    path('api/v1/', include(router.urls))
    # GENERIC MIXING CLASS VIEW START
    # path('articles/', ArticleList.as_view()),
    # path('articles/<slug:slug>/', ArticleDetails.as_view()),
    # GENERIC MIXING CLASS VIEW END
    # path('articles/', article_list),
    # path('articles/<slug:slug>/', article_details)
]