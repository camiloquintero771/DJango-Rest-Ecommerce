from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        update_user = super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user


class SomeFieldsUserSerializer(serializers.ModelSerializer):
    """ Clase para crear metodo que permita listar en el serializar campos
    especificos del modelo, al eliminar y actualizar la clase si utiliza
    todos los campos del modelo"""
    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],
            'password': instance['password']
        }


class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()

    def validated_name(self, value):
        if 'camilo' in value:
            raise serializers.ValidationError('Error')
        return value

    def validated_email(self, value):
        if value == "":
            raise serializers.ValidationError('Tiene que indicar correo')
        return value

    def validate(self, data):
        if data['name'] in data['email']:
             raise serializers.ValidationError('El email contiene el nombre')

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance