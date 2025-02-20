from django.urls import path, include
from .views import RegisterView, LoginView

urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('Login/', LoginView.as_view(), name='login' )

]




