from django.urls import path
from .views import *

urlpatterns = [
    path('login', handlelogin, name='login'),
    path('two_step/<str:token>', two_step, name='two_step'),
    path('logout', handleLogout, name='logout'),
    path('update_profile', update_profile, name='update_profile'),
    path('signup', signup, name='signup'),
]
