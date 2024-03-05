from django.contrib import admin
from django.urls import path
from app1.api import views


urlpatterns = [
    path('movie_list/',views.movie_list_av.as_view(),name="movie_list"),
    path('detail/<str:id>/',views.movie_detail_av.as_view(),name="movie_det")
]