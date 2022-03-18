
from apps.base.api import GeneralListApiView
from apps.products.api.serializers.general_serializers import \
    MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer

""" 
Vistas basada en clase para la API, su funcionalidad es listar
datos, heredan de GeneralListApiView. Posee el metodo get_queryset para 
realizar las consultas a la BD.
"""


class MeasureUnitListAPIView(GeneralListApiView):
    serializer_class = MeasureUnitSerializer


class CategoryProductListAPIView(GeneralListApiView):
    serializer_class = CategoryProductSerializer


class IndicatorListAPIView(GeneralListApiView):
    serializer_class = IndicatorSerializer

