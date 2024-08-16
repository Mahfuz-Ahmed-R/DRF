from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'colors', views.ColorViewSet, basename='color')
router.register(r'sizes', views.SizeViewSet, basename='size')
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'subcategories', views.SubCategoryViewSet, basename='subcategory')
router.register(r'products', views.ProductViewSet, basename='product')
router.register(r'orders', views.OrderViewSet, basename='order')
router.register(r'review-models', views.ReviewModelViewSet, basename='reviewmodel')

urlpatterns = [
    path('', include(router.urls)),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('update_item/', views.UpdateItemView.as_view(), name='update_item'),
    path('process_order/', views.ProcessOrderView.as_view(), name='process_order'),
    path('inventory/', views.InventoryView.as_view(), name='inventory'),
]