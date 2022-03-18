from rest_framework import generics


class GeneralListApiView(generics.ListAPIView):
    """
    Clase construida para abstraer la informacion necesaria que utiliza cada
    vista basada en clase, para listar datos a traves de a API.
    """
    """
    la funcion get_queryset realiza la consulta a la BD basandose en el modelo 
    que utilice el serializer_class, la funcion get_serializer obtiene la 
    clase serializador.
    """
    serializer_class = None

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(state=True)
