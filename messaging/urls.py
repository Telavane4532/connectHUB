from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('<str:username>/', views.conversation, name='conversation'),
]