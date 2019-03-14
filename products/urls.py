from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.index),
    path('<int:product_id>/', views.detail, name='detail'),
    path('post_url/', views.post_product, name='post_product'),
    path('<username>/', views.profile, name='profile'),
    path('new', views.new, name='new'),
]