from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework.authtoken.views import obtain_auth_token

from main.views import *

router = DefaultRouter()
router.register('actors', ActorViewSet)
router.register('movies', MovieViewSet)
router.register('comments', CommentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path("token/", obtain_auth_token),
    #path('actors/', ActorsAPIView.as_view()),
    #path('actors/<int:pk>/', ActorRetrieveAPIView.as_view()),
    #path('actors/<int:pk>/update/', ActorUpdateAPIView.as_view()),
    #path('actors/<int:pk>/delete/', ActorDeleteAPIView.as_view()),
    #path('actors/create/', ActorCreateAPIView.as_view()),
    #path('subscriptions/', SubscriptionAPIView.as_view()),
    #path('subscriptions/create/', SubscriptionCreateAPIView.as_view()),
    #path('subscriptions/<int:pk>/', SubscriptionRetrieveAPIView.as_view()),
    #path('movies/', MoviesAPIView.as_view()),
]
