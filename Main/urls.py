from django.conf.urls import url 
from Main import views
from django.urls import path,include
from rest_framework import routers

urlpatterns = [ 
    path('', views.BookView.as_view()),
    path('bookpost/',views.BookPostView.as_view()),
    path('book/<int:pk>',views.BookDetail.as_view())
]
