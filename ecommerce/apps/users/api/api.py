from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer, SomeFieldsUserSerializer


@api_view(['GET', 'POST'])
def user_api_view(request):
    """función para solicitar y crear elementos en la BD."""

    """METODO GET PARA ENVIAR SOLICITUD DE LISTA DE TODOS LOS ELEMENTOS"""
    if request.method == 'GET':
        # queryset
        user = User.objects.all()
        user_serializer = UserSerializer(user, many=True)
        
        return Response(user_serializer.data, status=status.HTTP_200_OK)
        # en el response si no se especifica, devuelve por default 200ok

    elif request.method == 'POST':
        """METODO POST PARA ENVIAR DATA Y CREAR INSTANCIAS EN LA BD
        convierte los daton de json en python mediante el UserSerializer"""

        user_serializer = UserSerializer(data=request.data)

        # validacion de los datos
        if user_serializer.is_valid():  # Valida los datos enviados en el Json
            user_serializer.save()  # Guarda la data validada
            print("usuario creado")
            return Response({'message': 'Usuario Creado correctamente!'},
                            status=status.HTTP_201_CREATED)
        # Si los datos no son válidos muestra error
        return Response(user_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk=None):
    """funcion para solicitar, actualizar y borrar mediante filtro inicial por
    PK UNA instancia de la BD. Se utiliza el filter() en la consulta inicial
    porque no arroja errores en caso de no encontrarse los datos (PK),
    no rompe el codigo, a diferencia del get()."""
    user = User.objects.filter(id=pk).first()

    if user:
        """METODO GET PARA SOLICITAR UNA INSTANCIA ESPECIFICA"""
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data)

        elif request.method == 'PUT':
            """METODO PUT PARA MODIFICAR UNA INSTANCIA ESPECIFICA"""
            user_serializer = UserSerializer(user, data=request.data)
            """user_serializer convierte los daton de json en python mediante 
            el UserSerializer.py y se pasan por parametros al UserSerializar la 
            instancia (user) y la data (data = request.data) que se desea 
            insertar"""
            if user_serializer.is_valid():
                """Valida los datos enviados en el Json"""
                user_serializer.save()
                """Guarda la data validada"""
                print("usuario creado")
                return Response(user_serializer.data,
                                status=status.HTTP_202_ACCEPTED)
            return Response(user_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
            # Si los datos no son válidos muestra error

        elif request.method == 'DELETE':
            """METODO DELETE PARA ELIMINAR UNA INSTANCIA ESPECIFICA"""
            user.delete()
            return Response({'message': 'Usuario ELiminado correctamente!'},
                            status=status.HTTP_200_OK)
    return Response({'message': 'No se ha encontrado usuario con estos datos'},
                    status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def user_some_fields_api_view(request):
    """función para solicitar y listar elementos especificos de la BD."""

    """METODO GET PARA ENVIAR SOLICITUD DE LISTA DE ELEMENTOS ESPECIFICOS"""
    if request.method == 'GET':
        # queryset
        user = User.objects.all().values('id', 'username', 'email', 'password')
        user_serializer = SomeFieldsUserSerializer(user, many=True)

        return Response(user_serializer.data, status=status.HTTP_200_OK)
        # en el response si no se especifica, devuelve por default 200ok
    elif request.method == 'POST':
        """METODO POST PARA ENVIAR DATA Y CREAR INSTANCIAS EN LA BD
        convierte los daton de json en python mediante el UserSerializer"""

        user_serializer = SomeFieldsUserSerializer(data=request.data)

        # validacion de los datos
        if user_serializer.is_valid():  # Valida los datos enviados en el Json
            user_serializer.save()  # Guarda la data validada
            print("usuario creado")
            return Response({'message': 'Usuario Creado correctamente!'},
                            status=status.HTTP_201_CREATED)
        # Si los datos no son válidos muestra error
        return Response(user_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class UserApiView(APIView):
    """ Utilizando Clases APIView"""

    def get(self, request):
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(UserSerializer.data)
