from django.urls import path
from .views import RegisterView,LoginView,prueba


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('prueba', prueba)
]