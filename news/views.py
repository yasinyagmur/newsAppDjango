from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Post
from .serializers import PostSerializers
# Create your views here.
def home(request):
    return HttpResponse('Blog app uygulamasına hoşgeldiniz...')


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class PostDetails(RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializers
