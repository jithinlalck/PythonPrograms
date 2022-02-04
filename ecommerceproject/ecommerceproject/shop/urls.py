from . import views
from django.urls import path
app_name='shop'

urlpatterns = [
    path('', views.fn_allProdCat, name='fn_allProdCat'),
    path('<slug:c_slug>/', views.fn_allProdCat, name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.fn_productDetail, name='product_cat_Detail')
]