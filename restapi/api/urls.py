from django.urls import path
from api.views import SignupUser,UserLogin




urlpatterns = [
    path('signup/',SignupUser.as_view(),name='signup'),
    path('login/',UserLogin.as_view(),name='login')
]