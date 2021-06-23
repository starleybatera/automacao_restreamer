from django.shortcuts import render
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, generics, serializers
from camera.models import Camera
from .serializers import CameraSerializer
from rest_framework.response import Response
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium  import webdriver
import time






class CameraViewSet(viewsets.ModelViewSet):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer

    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['id', 'descricao','url','agrupamento']
    
class Lista_Cameras(generics.ListAPIView):
    serializer_class =  CameraSerializer

    def get_queryset(self):
   
        time.sleep(2)
        navegador = webdriver.Remote( 'http://selenium:4444/wd/hub',desired_capabilities=DesiredCapabilities.CHROME)

        time.sleep(2)
        navegador.get("http://rasp-01.sa.ngrok.io/")
        username = navegador.find_element_by_id("input_username")
        password = navegador.find_element_by_id("input_password")
        username.send_keys("admin")
        password.send_keys("datarhei")

        time.sleep(1)

        button_login = navegador.find_element_by_xpath("//*[@type='submit']")
        button_login.submit()

        time.sleep(3)

        navegador.find_element_by_xpath('//*[@id="content"]/div[4]/label/input').click()

        time.sleep(2)

        navegador.find_element_by_xpath('//*[@id="content"]/div[7]/div/div').click()

        time.sleep(90)

        navegador.find_element_by_xpath('//*[@id="content"]/div[7]/div[1]').click()
        

        user = self.request.user
       

        return Camera.objects.filter(agrupamento__fazenda__usuario_fazenda__usuario=user.id).order_by('id')

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.request.user
        
        if user.is_superuser:
            camera = serializer.save()
            return Response({"Results":CameraSerializer(camera, context=self.get_serializer_context()).data,})
        else:
            raise serializers.ValidationError({'Error': 'Usuário sem autorização para cadastrar!'})
