from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer


@api_view(['GET', 'POST'])
def user_api_view(request):
    #    Utilizando funciones para crear la vista de la API
    #   metodo GET para enviar solicitud y que devuelva la data
    if request.method == 'GET':
        user = User.objects.all()
        user_serializer = UserSerializer(user, many=True)
        return Response(user_serializer.data)

    #   metodo POST para enviar data y crear en la base de datos instancias
    elif request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():  # Valida los datos enviados en el Json
            user_serializer.save()  # Guarda la data validada
            print("usuario creado")
            return Response(user_serializer.data,
                            # Responde la data creada
                            status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors)
        # Si los datos no son válidos muestra error


@api_view(['GET'])
def user_detail_api_view(request, pk=None):
    #   metodo GET para solicitar una instancia específica de la data
    if request.method == 'GET':
        # filtro por PK, el filter() no arroja errores, valida la instancia
        # si no encuentra el PK, no rompe el codigo, a diferencia del get()
        user = User.objects.filter(id=pk).first()
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)


class UserApiView(APIView):
    """ Utilizando Clases APIView"""

    def get(self, request):
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(UserSerializer.data)
