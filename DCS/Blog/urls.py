from django.urls import path
from .views import PostDetailView

urlpatterns = [
    path('post/<int:pk>/detail/', PostDetailView, name="post_detail")
]