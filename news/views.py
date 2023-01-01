from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Post
from .serializers import PostSerializers
from .pagination import CustomCursorPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter


def home(request):
    return HttpResponse('Blog app uygulamasına hoşgeldiniz...')

class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

    # pagination
    pagination_class = CustomCursorPagination
    
    # filter 
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category_id','status']  # setting ile views de burası birlikte çalışıyor filtreleme için
    
    # search
    # search_fields = ['title', 'category_id','status']


class PostDetails(RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializers
