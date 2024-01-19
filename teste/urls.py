from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name= 'index'),

    path('listar_Aluno', views.listar_Aluno, 
         name='listar_Alunos'),
    
    path('lista_cursos', views.listar_cursos,
         name='listar_cursos'),

    path('incluir_aluno', views.incluir_aluno,
         name='incluir_aluno'),

    path('editar_aluno/<int:id>', views.editar_aluno,
         name='editar_aluno'),
    path('incluir_curso', views.incluir_curso,
         name='incluir_curso'),

    path('editar_curso/<int:id>', views.editar_curso,
         name='editar_curso')

]