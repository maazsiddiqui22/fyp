from django.urls import path
from . import views


urlpatterns =[
    path('',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('register_user/',views.register_user,name='register_user'),
    path('detect/',views.detect,name='detect'),

]