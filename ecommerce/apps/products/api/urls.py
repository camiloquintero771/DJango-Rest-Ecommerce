from django.urls import path
from apps.products.api.views.general_view import MeasureUnitListAPIView, \
    CategoryProductListAPIView, IndicatorListAPIView
from apps.products.api.views.products_views import ProductListApiView

urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name='measure_unit'),
    path('category_product/', CategoryProductListAPIView.as_view(),
         name='category_product'),
    path('indicator/', IndicatorListAPIView.as_view(),
         name='indicator'),
    path('products/', ProductListApiView.as_view(),
         name='Products')
]
