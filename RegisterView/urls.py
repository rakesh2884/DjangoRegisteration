from django.urls import path
from RegisterView import views

urlpatterns = [
    path('register',
         views.register.as_view(),
         name='register'),
    path('Login',
         views.Login.as_view(),
         name='login'),
         ]
