# appname/urls.py
from django.urls import path
from .views import ItemListCreateView, ItemRetrieveDestroyView

urlpatterns = [
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemRetrieveDestroyView.as_view(), name='item-retrieve-destroy'),
]
