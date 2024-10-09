from django.urls import path
from core import views

urlpatterns = [
    path('livros/', views.LivroList.as_view(), name='livros-list'),
    path('livros/<int:pk>/', views.LivroDetail.as_view(), name='livrodetail'),

    path('categorias/', views.CategoriaList.as_view(), name='categorias-list'),
    path('categorias/<int:pk>/', views.CategoriaDetail.as_view(), name='categoriasdetail'),

    path('autores/', views.AutorList.as_view(), name='autores-list'),
    path('autores/<int:pk>/', views.AutorDetail.as_view(), name='autoresdetail'),
]
