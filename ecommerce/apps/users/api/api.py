from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer


@api_view(['GET', 'POST']) # Utilizando funciones para crear la vista de la API
def user_api_view(request):

    # METODO GET PARA ENVIAR SOLICITUD DE TODOS LOS ELEMENTOS
    if request.method == 'GET':
        user = User.objects.all()
        user_serializer = UserSerializer(user, many=True)
        return Response(user_serializer.data)

    # METODO POST PARA ENVIAR DATA Y CREAR INSTANCIAS EN LA BD
    elif request.method == 'POST':
        #   convierte los daton de json en python mediante el UserSerializer
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():  # Valida los datos enviados en el Json
            user_serializer.save()  # Guarda la data validada
            print("usuario creado")
            return Response(user_serializer.data,
                            # Responde la data creada
                            status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors)
        # Si los datos no son válidos muestra error


@api_view(['GET', 'PUT'])
def user_detail_api_view(request, pk=None):
    # METODO GET PARA SOLICITAR UNA INSTANCIA ESPECIFICA
    if request.method == 'GET':
        user = User.objects.filter(id=pk).first()
        # filtro por PK, el filter() no arroja errores, valida la instancia
        # si no encuentra el PK, no rompe el codigo, a diferencia del get()
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)

    # METODO PUT PARA MODIFICAR UNA INSTANCIA ESPECIFICA
    elif request.method == 'PUT':
        user = User.objects.filter(id=pk).first()
        user_serializer = UserSerializer(user, data=request.data)
        # convierte los daton de json en python mediante el UserSerializer
        # se pasan por parametros al UserSerializar la instancia (user) y la
        # data (data = request.data) que se desea insertar

        if user_serializer.is_valid():  # Valida los datos enviados en el Json
            user_serializer.save()  # Guarda la data validada
            print("usuario creado")
            return Response(user_serializer.data,
                            status=status.HTTP_202_ACCEPTED)
        return Response(user_serializer.errors)
        # Si los datos no son válidos muestra error


class UserApiView(APIView):
    """ Utilizando Clases APIView"""

    def get(self, request):

        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(UserSerializer.data)
