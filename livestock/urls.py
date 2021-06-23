
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings 
from rest_framework import routers
from usuario.api.viewset import UserViewSet, GetTokenViewSet, RegisterAPI,LoginAPI, ChangePasswordView
from animais.api.viewset import AnimalViewSet, Lista_Animais, Lista_Animal
from camera.api.viewset import CameraViewSet, Lista_Cameras
from fazenda.api.viewset import FazendaIndividual, FazendaViewSet
from usuario_fazenda.api.viewset import Usuario_FazendaViewSet, Lista_Fazenda_Usuario
from agrupamentos.api.viewset import AgrupamentoViewSet, Lista_Agrupamentos
from historico.api.viewset import HistoricoViewSet, Lista_Historicos, Lista_Historico, Lista_Historico_Notificacoes
from historico_tipo.api.viewset import Historico_TipoViewSet
from raca.api.viewset import RacaViewSet
from notificacao.api.viewset import NotificacaoViewSet, Lista_Notificacoes, Lista_Notificacao, Lista_Agrupamentos_Notificacoes
from imagens.api.viewset import ImagensViewSet, Lista_Imagens, Lista_Imagem
from rest_framework.authtoken.views import obtain_auth_token
from knox import views as knox_views





router = routers.SimpleRouter()
router.register(r'usuarios', UserViewSet)
router.register(r'animais', AnimalViewSet)
router.register(r'fazendas', FazendaViewSet)
router.register(r'historicos', HistoricoViewSet)
router.register(r'historicos_tipos', Historico_TipoViewSet)
router.register(r'racas', RacaViewSet)
router.register(r'imagens', ImagensViewSet)
router.register(r'users', UserViewSet)
router.register(r'notificacoes', NotificacaoViewSet)
# router.register(r'usuarios_fazendas', Usuario_FazendaViewSet)
# router.register(r'agrupamentos', AgrupamentoViewSet)
# router.register(r'cameras', CameraViewSet)




urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('rest_auth/', include('rest_auth.urls')),
    path('cadastro/', RegisterAPI.as_view(), name = 'cadastro'),
    path('login/', LoginAPI.as_view(), name = 'login'),
    path('logout/', knox_views.LogoutView.as_view(), name = 'logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name = 'logoutall'),
    path('resetpassword/', ChangePasswordView.as_view(), name = 'resetpassword'),
    path('usuarios_fazendas/', Lista_Fazenda_Usuario.as_view(), name = 'list_fazenda_usuario'),
    path('agrupamentos/', Lista_Agrupamentos.as_view(), name = 'list_agrupamentos'),
    path('cameras/', Lista_Cameras.as_view(), name = 'list_cameras'),
    path('fazenda/<int:id>/', FazendaIndividual.as_view(),name='fazenda_individual'),
    path('animal/<str:identificacao>/', Lista_Animais.as_view(),name='list_animal'),
    path('animal/<str:identificacao>/<int:id>/', Lista_Animal.as_view(), name='list_animal'),
    path('historico/<int:id_animal>/', Lista_Historicos.as_view(),name='historico_animal'),
    path('historico/<int:id>/<int:id_animal>/', Lista_Historico.as_view(), name='historico_animal'),
    path('historicos/status/<str:status>/', Lista_Historico_Notificacoes.as_view(),name='notificacoes'),
    path('imagem/<int:cod_animal>/', Lista_Imagens.as_view(),name='imagens_animal'),
    path('imagem/<int:cod_animal>/<int:id>/', Lista_Imagem.as_view(), name='imagem_animal'),
    path('notificacao/<int:id_agrupamento>/', Lista_Notificacoes.as_view(),name='notificacao_agrupamento'),
    path('notificacao/<int:id>/<int:id_agrupamento>/', Lista_Notificacao.as_view(),name='notificacao_agrupamento'),
    path('notificacao/status/<str:status>/', Lista_Agrupamentos_Notificacoes.as_view(),name='notificacao_agrupamento_status'),

    # path('get_token/', GetTokenViewSet.as_view(),name='token_user'),
    # path('rest_auth/login/', include('rest_auth.registration.urls'), name = 'login_user'),
    # path('rest_auth/registration/', include('rest_auth.registration.urls'), name = 'register_user'),
    # path('rest_auth/password/reset/', include('rest_auth.registration.urls'), name = 'reset_password'),
    # path('rest-auth/password/reset/confirm/', include('rest_auth.registration.urls'), name = 'reset_password_confirm'),
    # path('rest-auth/password/change/', include('rest_auth.registration.urls'), name = 'change_password'),
    # path('api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api-token-auth/', obtain_auth_token),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
