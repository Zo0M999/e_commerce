from django.urls import path
from . import views


app_name = 'store'
urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:prod_id>', views.product, name='product'),
    path('category/<int:category_id>', views.category, name='category'),
    path('about/', views.about, name='about'),
]