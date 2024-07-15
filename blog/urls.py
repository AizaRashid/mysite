from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.PostListView.as_view(),name='post_list'),
    path('about/',views.about,name='about'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('add/category/', views.AddCategoryView.as_view(), name='add_category'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('category/<str:cats>/',views.CategoryView,name='category'),
    path('like/<int:pk>/',views.LikeView,name="like_post"),
    path('category_list/',views.CategoryListView,name="category_list"),
    path('authorprofile/<int:author_id>/',views.authorprofile,name='author_profile'),
    path('author/<int:author_id>/follow/',views.follow_toggle,name='follow_toggle'),
    ]

