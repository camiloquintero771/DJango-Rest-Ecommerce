from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel


class MeasureUnit(BaseModel):
    """ Modelo para crear unidades de medida"""
    """contiene las funiciones _history_user para lograr resgitrar cual usuario 
     realizo el cambio en el modelo """
    description = models.CharField('Descripción', max_length=50, blank=False,
                                   null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Unidad de medida'
        verbose_name_plural = 'Unidades de medida'

    def __str__(self):
        return self.description


class CategoryProduct(BaseModel):
    """ Modelo para crear categorias de producto"""
    """contiene las funiciones _history_user para lograr resgitrar cual usuario 
     realizo el cambio en el modelo """
    description = models.CharField('Descripción', max_length=50, blank=False,
                                   null=False, unique=True)

    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Categoria de producto'
        verbose_name_plural = 'Categoria de productos'

    def __str__(self):
        return self.description


class Indicator(BaseModel):
    """ Modelo para crear los de descuentos que se asignan a cada categorias
    de los productos.
    Contiene las funciones _history_user para lograr resgitrar cual usuario
    realizo el cambio en el modelo """

    descount_value = models.PositiveSmallIntegerField(
        default=0, verbose_name='Valor de descuento')
    category_product = models.ForeignKey(CategoryProduct,
                                         on_delete=models.CASCADE,
                                         verbose_name='Categoria de producto')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Indicador de oferta '
        verbose_name_plural = 'Indicador de ofertas'

    def __str__(self):
        return f'Oferta de la categoria{self.category_product} : ' \
               f'{self.descount_value}%'


class Product(BaseModel):
    """ Modelo para crear los productos.
    Contiene las funiciones _history_user para lograr resgitrar cual usuario
    realizo el cambio en el modelo """

    name = models.CharField('Nombre producto', max_length=150, unique=True,
                            blank=False, null=False)
    description = models.TextField('Descripcion de producto', blank=False,
                                   null=False)
    image = models.ImageField('Imagen del producto',
                              upload_to='products/',
                              blank=True, null=True)
    measureunit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE,
                                    verbose_name='Unidad de medida')
    category_product = models.ForeignKey(CategoryProduct,
                                         on_delete=models.CASCADE,
                                         verbose_name='Categoria de producto')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Producto '
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name
