from django.urls import path
from . import views


urlpatterns =[
    path('/',views.home,name='home'),
    path('/<mood>/',views.home,name='home'),
    
    path('/new_search/',views.new_search,name='new_search'),
    # path('<mood>/new_search/',views.new_search,name='new_search'),
]