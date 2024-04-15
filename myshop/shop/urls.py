from django.urls import path,include

from .views import product_list, product_detail,ProductViewSet,CategoryViewSet
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register('products',ProductViewSet,basename='products')

router = DefaultRouter()
router.register('categories',CategoryViewSet,basename='category')

app_name='shop'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<slug:category_slug>/', product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', product_detail, name='product_detail'),
    path('shop/product_viewset/',include(routers.urls)),
    path('shop/category_viewset/',include(router.urls)),

]