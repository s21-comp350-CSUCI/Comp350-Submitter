from django.urls import path
from . import views

urlpatterns = [
    path('', views.createaccount, name='createaccount'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('login', views.login, name='login'),
    path('event-create', views.eventCreate, name='eventCreate'),
    path('event-modify', views.eventModify, name='eventModify'),
    path('logout', views.logout, name='logout'),
    path('submit-python', views.submitPython, name='submitPython'),
    path('submit-token', views.submitToken, name='submitToken'),
]