from django.urls import path

from .views import SignInView


app_name = "accounts"

urlpatterns = [
    path('sign-in', SignInView.as_view(), name='sign_in'),
]