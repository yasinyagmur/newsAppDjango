from django.urls import path
from .views import PostList,PostDetails, CategoryView,home


urlpatterns = [
    path('',home),

    #! concrete
    path("post/", PostList.as_view()),
    path("post/<int:pk>", PostDetails.as_view()),
    path("category/", CategoryView.as_view()),
]
