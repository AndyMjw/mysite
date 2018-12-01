from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/news/
    path('', views.news_list, name="news_list"),
    # localhost:8000/news/1/
    path('<int:news_id>', views.news_detail, name="news_detail"),
]
