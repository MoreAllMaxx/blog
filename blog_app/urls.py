from django.urls import path
from .views import MainPageView, PostDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, \
    category_view, CategoryList, like_view

urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
    path('article/id<int:pk>', PostDetailView.as_view(), name='article-detail'),
    path('add_post', AddPostView.as_view(), name='add-post'),
    path('add_category', AddCategoryView.as_view(), name='add-category'),
    path('article/id<int:pk>/update_post', UpdatePostView.as_view(), name='update-post'),
    path('article/id<int:pk>/delete_post', DeletePostView.as_view(), name='delete-post'),
    path('category/<str:category>', category_view, name='category'),
    path('categories', CategoryList.as_view(), name='categories'),
    path('like/<int:pk>', like_view, name='like-post')
]
