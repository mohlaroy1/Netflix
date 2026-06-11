from django.contrib import admin
from django.urls import path

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('actors/', ActorsAPIView.as_view()),
    path('actors/<int:pk>/', ActorRetrieveAPIView.as_view()),
    path('actors/create/', ActorCreateAPIView.as_view()),
    path('subscriptions/', SubscriptionAPIView.as_view()),
    path('subscriptions/create/', SubscriptionCreateAPIView.as_view()),
    path('subscriptions/<int:pk>/', SubscriptionRetrieveAPIView.as_view()),
]
