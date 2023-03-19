from django.urls import path
from posts.views import (
    post_list,
    post_add_view,
    post_edit_view,
    post_delete_view,
    post_home,
    post_detail_view,
)


app_name = "posts"
urlpatterns = [
    path("", post_home, name="posthome"),
    path("posts-list/", post_list, name="postslist"),
    path("posts-add/", post_add_view, name="posts_add"),
    path("posts/<int:postid>/", post_detail_view, name="posts_detail"),
    path("posts-edit/<int:postid>", post_edit_view, name="posts_edit"),
    path("post-delete/", post_delete_view, name="posts_delete"),
]
