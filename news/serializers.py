from rest_framework import serializers
from .models import Category,Post


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model =Category
        fields = ['name','id']
    
    # blog_posts = CategorySerializers(many=True)
    # blog_posts = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only =True,
    #     view_name = 'post'
    # )

class PostSerializers(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'