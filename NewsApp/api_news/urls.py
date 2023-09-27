from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name="login_page"),
    path('login', views.login, name="login"),
    path('home', views.get_news, name="home"),
    path('search', views.search, name="search"),
    path('history', views.get_history, name="history"),
]