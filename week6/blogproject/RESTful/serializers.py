from .models import *
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer) :

    class Meta : 
        model = Post
        fields = ('title', 'postDate', 'content')
        # fields = "__all__"
    