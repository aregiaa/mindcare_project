from django.contrib import admin
from django.urls import path
from app.views import *
from app.views import CustomLoginView 
from django.shortcuts import redirect

# Redireciona para a página de login quando a URL raiz é acessada
def redirect_to_login(request):
    return redirect('login')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_login),  # Redireciona a URL raiz para o login
    path('login', LoginView.as_view(), name='login'),  # Página de login
    path('home/', HomeView.as_view(), name='home'),  # Página inicial após login
    path('register', RegisterView.as_view(), name='register'),
    path('agendar_sessao', AgendamentoView.as_view(), name='agendar_sessao'),
    path('agendamentos', ListarAgendamentosView.as_view(), name='agendamentos'),   
    path('cidades', CidadeView.as_view(), name='cidades'),
    path('ocupacoes', OcupacaoView.as_view(), name='ocupacoes'),
    path('pacientes', PacienteView.as_view(), name='pacientes'),
    path('profissionais', ProfissionalView.as_view(), name='profissionais'),
    path('instituicoes', InstituicaoView.as_view(), name='instituicoes'),
    path('logout', LoginView.logout_user, name='logout'), 
    path('horarios', HorarioView.as_view(), name='horarios')
]
