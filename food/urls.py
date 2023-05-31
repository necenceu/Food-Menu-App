from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    # main page of the website
    path('', views.IndexClassView.as_view(), name='index'),

    # detail of item
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),

    # some item path to test fucntionality
    path('item/', views.item, name='item'),

    # adding item
    path('add', views.add_item, name='add_item'),

    # editing item
    path('update/<int:id>/', views.update_item, name='update_item'),

    # deleting item
    path('delete/<int:id>/', views.delete_item, name='delete_item'), 
]