from .models import Cidade, Ocupacao, Paciente, Profissional, Agendamentos, Instituicao, Horario
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = 'login' 



from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login.html'  
    redirect_authenticated_user = True  


class Index(View):
    def get(self, request):
        return render(request, 'index.html')
    def post(self, request):
        pass

class CidadeView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidades.html', {'cidades': cidades})
    
class OcupacaoView(View):
    def get(self, request, *args, **kwargs):
        ocupacoes = Ocupacao.objects.all()
        return render(request, 'ocupacoes.html', {'ocupacoes': ocupacoes})
    
class PacienteView(View):
    def get(self, request, *args, **kwargs):
        pacientes = Paciente.objects.all()
        return render(request, 'pacientes.html', {'pacientes': pacientes})

class ProfissionalView(View):
    def get(self, request, *args, **kwargs):
        profissionais = Profissional.objects.all()
        return render(request, 'profissionais.html', {'profissionais': profissionais})


class InstituicaoView(View):
    def get(self, request, *args, **kwargs):
        instituicoes = Instituicao.objects.all()
        return render(request, 'instituicoes.html', {'instituicoes': instituicoes})
class LoginView(View):
    def get(self, request):
        
        return render(request, 'login.html') 
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home.html')
        
        messages.error(request, 'Usuário ou senha inválidos')
        return render(request, 'login.html', {'error':'Usuário ou senha inválidos'})
    
    def logout_user(request):
        logout(request)
        return render(request, 'login.html')

class RegisterView(View):
    def get(self, request):
        ocupacoes = Ocupacao.objects.all()
        cidades = Cidade.objects.all()
        instituicoes = Instituicao.objects.all()
        return render(request, 'register.html', {'ocupacoes': ocupacoes, 'cidades': cidades, 'instituicoes': instituicoes})
    
    
    def post(self, request):
        
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.create_user(username=username, password=password)
            user.save()
            
            nome = request.POST.get('nome')
            cpf = request.POST.get('cpf')
            data = request.POST.get('data')
            telefone = request.POST.get('telefone')
            endereco = request.POST.get('endereco')
            cidade_id = request.POST.get('cidade')
            pais = request.POST.get('pais')
            cep = request.POST.get('cep')
            ocupacao_id = request.POST.get('ocupacao')
            instituicao_id = request.POST.get('instituicao')
            
            cidade_user = Cidade.objects.get(id=cidade_id)
            ocupacao_user = Ocupacao.objects.get(id=ocupacao_id)
            instituicao_user = Instituicao.objects.get(id=instituicao_id)

            if ocupacao_user.nome == 'Psicólogo' or ocupacao_user.nome == 'Orientador':
                profissional = Profissional()
                profissional.user = user
                profissional.nome = nome
                profissional.cpf = cpf
                profissional.data_nascimento = data
                profissional.telefone = telefone
                profissional.endereco = endereco
                profissional.cidade = cidade_user
                profissional.pais = pais
                profissional.cep = cep
                profissional.ocupacao = ocupacao_user
                profissional.instituicao = instituicao_user
                profissional.save()

            else:
                paciente = Paciente()
                paciente.user = user
                paciente.nome = nome
                paciente.cpf = cpf
                paciente.data_nascimento = data
                paciente.telefone = telefone
                paciente.endereco = endereco
                paciente.cidade = cidade_user
                paciente.pais = pais
                paciente.cep = cep
                paciente.ocupacao = ocupacao_user
                paciente.instituicao = instituicao_user
                paciente.save()


            return render(request, 'login.html')
        

@method_decorator(login_required, name='dispatch')
class AgendamentoView(View):
    def get(self, request):

        profissionais = Profissional.objects.filter(ocupacao__nome__in=['Psicólogo', 'Orientador'])
        horarios = Horario.objects.all()  
        instituicoes = Instituicao.objects.all()  

        return render(request, 'agendar_sessao.html', {
            'profissionais': profissionais,
            'horarios': horarios,
            'instituicoes': instituicoes,
        })

    def post(self, request):
        
        profissional_id = request.POST.get('profissional')
        horario_id = request.POST.get('horario')
        instituicao_id = request.POST.get('instituicao')
        observacoes = request.POST.get('observacoes')

        
        paciente = get_object_or_404(Paciente, user=request.user)

        profissional = get_object_or_404(Profissional, id=profissional_id)
        horario = get_object_or_404(Horario, id=horario_id)
        instituicao = get_object_or_404(Instituicao, id=instituicao_id)
        print(profissional, horario, instituicao)
    
        print(horario)
        agendamento = Agendamentos()
        agendamento.paciente = paciente
        agendamento.profissional = profissional
        agendamento.horario = horario
        agendamento.instituicao = instituicao
        agendamento.observacoes = observacoes
        agendamento.save()
        
        messages.success(request, 'Agendamento realizado com sucesso!')
        return redirect('home')
    
@method_decorator(login_required, name='dispatch')
class ListarAgendamentosView(View):
    def get(self, request):
        try:
            paciente = Paciente.objects.get(user=request.user)
            agendamentos = Agendamentos.objects.filter(paciente=paciente)
        except Paciente.DoesNotExist:
            try:
                profissional = Profissional.objects.get(user=request.user)
                agendamentos = Agendamentos.objects.filter(profissional=profissional)
            except Profissional.DoesNotExist:
                agendamentos = None 

        return render(request, 'agendamentos.html', {'agendamentos': agendamentos})
    
class HorarioView(View):
    def get(self, request):
        horarios = Horario.objects.all()
        return render(request, 'horarios.html', {'horarios': horarios})
    
    def post(self, request):
        hora = request.POST.get('hora')
        data = request.POST.get('data')
        profissional_id = request.POST.get('profissional')
        
        profissional = Profissional.objects.get(id=profissional_id)
        
        horario = Horario()
        horario.hora = hora
        horario.data = data
        horario.profissional = profissional
        horario.save()
        
        return render(request, 'index.html')
    
    