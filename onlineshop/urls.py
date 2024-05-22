from django.urls import path
from .views import ListCreateView, DetailUpdateView


urlpatterns = [
    path('product/', ListCreateView.as_view() , name = 'product'),
    path('detail/<int:pk>', DetailUpdateView.as_view() , name = 'detail'),
]