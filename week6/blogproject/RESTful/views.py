from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.filters import SearchFilter
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication
from datetime import datetime


class PostViewSet(viewsets.ModelViewSet) :

    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filter_backends = [SearchFilter]
    search_fields = ("title", "content")

    def get_queryset(self):
        qs = super().get_queryset()
        # if self.request.user.is_authenticated :
        #     qs = qs.filter(author = self.request.user)
        # else :
        #     qs = qs.none()
        return qs

    def perform_create(self, serializer):
        # serializer.save(author = self.request.user)
        serializer.save()
    
    def perform_update(self, serializer):
        # serializer.save(author = self.request.user, postDate = datetime.now())
        serializer.save(postDate = datetime.now())