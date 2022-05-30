from django.urls import path
from .views import *
# from rest_auth.views import LoginView, LogoutView
# from rest_auth.registration.views import RegisterView

blogList = PostViewSet.as_view({
    'get' : 'list',
    'post' : 'create'
})

blogDetail = PostViewSet.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'patch' : 'partial_update',
    'delete' : 'destroy'
})


urlpatterns = [

    # path('login', LoginView.as_view()),
    # path('logout', LogoutView.as_view()),
    # path('register', RegisterView.as_view()),
    path('blog', blogList),
    path('blog/<int:pk>', blogDetail),

]