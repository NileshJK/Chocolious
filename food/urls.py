from .import views
from django.urls import path

urlpatterns=[
    path('',views.fun_food,name='food_function'),
    path('item/',views.item,name='item'),
]