from api.views import *
from django.urls import path





urlpatterns = [
    path('cursos/',CursosView.as_view(),name ='Cursos'),
    path('cursos/creat',CreateCursosView.as_view(),name="add curso"),
    path('cursos/<str:filtro>',CursosViewFilter.as_view(),name="filter curso"),
    path('cursos2/',CursosView2.as_view(),name ='Cursos2'),
    
  
    
]