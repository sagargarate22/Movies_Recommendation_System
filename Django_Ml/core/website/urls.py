from django import urls
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('autocomplete/',views.autocomplete,name='autocomplete'),
    path('recommend/',views.recommend,name='recommend'),
    path('recommend_movie/<str:movie_name>/',views.recommend_movies,name='recommend_movie'),
    path('logout/',views.logout_user,name='logout'),
    path('signup/',views.signup_user,name='signup'),
]
