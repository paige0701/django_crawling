from django.urls import path

from baseball import views

urlpatterns = [
    path('', view=views.score_board, name='score_board')
]