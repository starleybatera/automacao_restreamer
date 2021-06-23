from rest_framework import viewsets, permissions, generics
from rest_framework.generics import UpdateAPIView
from django.contrib.auth import login
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from .serializers import UsuarioSerializer, RegisterSerializer, UserPasswordChangeSerializer
from rest_framework.views import APIView
from rest_framework import status, serializers
from knox.models import AuthToken



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
   

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.request.user
        if user.is_superuser:
            usuario = serializer.save()
            return Response({"User":UsuarioSerializer(usuario, context=self.get_serializer_context()).data,"token": AuthToken.objects.create(user)[1], "message": "User successfully registered !", "status":"ok"})
        else:
            raise serializers.ValidationError({'Restrição': 'Usuário não tem autorização para cadastrar!'})

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        id = user.id
        username = user.username
        email = user.email
        login(request, user)
        temp_list=super(LoginAPI, self).post(request, format=None)
        temp_list.data["id"] = id
        temp_list.data["username"] = username
        temp_list.data["email"] = email
       

        return Response({"data":temp_list.data})

class ChangePasswordView(UpdateAPIView):
    permission_classes = (permissions.AllowAny,)
    model = User
    serializer_class = UserPasswordChangeSerializer
    

    def get_object(self, queryset=None):
        print(self.request.user)
        return self.request.user

    
   

class GetTokenViewSet(ObtainAuthToken):
   
    def post(self, request, *args, **kwargs):
        response = super(GetTokenViewSet, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        user_serializer = UsuarioSerializer(user, many=False)
        return Response({'token': token.key, 'user':user_serializer.data})


