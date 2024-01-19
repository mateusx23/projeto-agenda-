from django.shortcuts import redirect, render
from django.http import HttpResponse
from teste.forms import AlunoForm, CursoForm
from teste.models import Aluno,Curso
# Create your views here.

def index(request):
    return HttpResponse("ola mundo! agora voce e web")

def listar_Aluno(request):
    Alunos = Aluno.objects.all()
    return render(request, 'listaralunos.html',
                {'alunos': Alunos})

def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'listarcursos.html',
                {'cursos':cursos})

def incluir_aluno(request):
    if request.method =='POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_Alunos')
    form = AlunoForm()
    return render(request, 'incluir_alunos.html',
                {'form': form})    

def editar_aluno(request,id):
    aluno = Aluno.objects.get(id=id)
    form = AlunoForm(instance=aluno)
    if request.method == 'POST':
        form = AlunoForm(request.POST,instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('listar_Alunos')
        
    return render(request, 'incluir_alunos.html',
                  {'form': form})

def editar_curso(request,id):
    Curso = Curso.objects.get(id=id)
    form = CursoForm(instance=Curso)
    if request.method == 'POST':
        form = CursoForm(request.POST,instance=Curso)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
        
        return render(request, 'incluir_curso.html',
                      {'form': form})

def incluir_curso(request):
    if request.method =='POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    form = CursoForm()     

    return render(request,'incluir_curso.html',
                  {'form': form})


def excluir_aluno(request,id):
    aluno = Aluno.objects.get(id=id)
    aluno.delete()
    return redirect('listar_Alunos')

def excluir_curso(request,id):
    aluno = Curso.objects.get(id=id)
    aluno.delete()
    return redirect('listar_cursos')