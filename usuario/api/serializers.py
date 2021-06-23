from rest_framework import serializers
from rest_framework.serializers import Serializer
from django.contrib.auth.models import User


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email','is_superuser')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','is_superuser')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        if validated_data['is_superuser'] == True:
            user = User.objects.create_superuser(validated_data['username'], validated_data['email'], validated_data['password'])
        else:
            user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class UserPasswordChangeSerializer(Serializer):

    old_password = serializers.CharField(required=True, max_length=30)
    password = serializers.CharField(required=True, max_length=30)
    confirmed_password = serializers.CharField(required=True, max_length=30)

    def validate(self, data):

        if not self.context['request'].user.check_password(data.get('old_password')):
            raise serializers.ValidationError({'old_password': 'Wrong password.'})

        if data.get('confirmed_password') != data.get('password'):
            raise serializers.ValidationError({'password': 'Password must be confirmed correctly.'})

        return data

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

    def create(self, validated_data):
        pass

    @property
    def data(self):
        return {'status': 'ok', 'password': 'password changed successfully!'}