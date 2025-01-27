from django.urls import path
from . import views


app_name = 'store'
urlpatterns = [
    path('', views.home, name='home'),
    path('all_products/', views.all_products, name='all_products'),
    path('product/<int:prod_id>', views.product, name='product'),
    path('category/<int:category_id>', views.category, name='category'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
]