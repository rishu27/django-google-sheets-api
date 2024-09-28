from django.urls import path
from .views import UserDataView

urlpatterns = [
    path('api/userdata/', UserDataView.as_view(), name='user_data_api'),
]