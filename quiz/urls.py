from django.urls import path

from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.index, name='index'),
    
    path('add_question', views.add_question, name='add_question'),
    
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
   

    
]
