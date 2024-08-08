from django.urls import path, include
from blog.views import (PostListView,about,PostDetailView,CreatePostView,AddCategoryView,
PostUpdateView,DraftListView,PostDeleteView,post_publish,add_comment_to_post,comment_approve,
comment_remove,CategoryView,LikeView,CategoryListView,authorprofile,follow_toggle,home,top)
urlpatterns=[
    path('',top,name='top'),
    path('postlist/',PostListView.as_view(),name='post_list'),
    path('about/',about,name='about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', CreatePostView.as_view(), name='post_new'),
    path('add/category/', AddCategoryView.as_view(), name='add_category'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('drafts/', DraftListView.as_view(), name='post_draft_list'),
    path('post/<int:pk>/remove/', PostDeleteView.as_view(), name='post_remove'),
    path('post/<int:pk>/publish/', post_publish, name='post_publish'),
    path('post/<int:pk>/comment/', add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/',comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', comment_remove, name='comment_remove'),
    path('category/<str:cats>/',CategoryView,name='category'),
    path('like/<int:pk>/',LikeView,name="like_post"),
    path('category_list/',CategoryListView,name="category_list"),
    path('authorprofile/<int:author_id>/',authorprofile,name='author_profile'),
    path('author/<int:author_id>/follow/',follow_toggle,name='follow_toggle'),
    ]