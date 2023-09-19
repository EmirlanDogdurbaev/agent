from django.urls import path
from .views import RegistrationAPIView, UserLoginAPIView, RegistrationProducerAPIView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('register/company/', RegistrationProducerAPIView.as_view(), name="register/company")
]
