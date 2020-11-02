from django.urls import path

from .views import (
    PlayerListView,
    PlayerUpdateView,
    PlayerDetailView,
    PlayerDeleteView,
    PlayerCreateView,
    refreeListView,
    refreeDetailView,
    stadiumListView,
    stadiumDetailView
    )

urlpatterns = [
    path('', PlayerListView.as_view(), name='player_list'),
    path('<int:pk>/edit/',
         PlayerUpdateView.as_view(), name='player_edit'),
    path('<int:pk>/delete/',
         PlayerDeleteView.as_view(), name='player_delete'),
    path('<int:pk>/',
         PlayerDetailView.as_view(), name='player_detail'),
    path('new/', PlayerCreateView.as_view(), name='player_new'),
    path('refree/', refreeListView.as_view(), name='refree_list'),
path('/refree/<int:pk>/',
         refreeDetailView.as_view(), name='refree_detail'),
    path('stadium/', stadiumListView.as_view(), name='stadium_list'),
path('/stadium/<int:pk>',
         stadiumDetailView.as_view(), name='stadium_detail'),


]