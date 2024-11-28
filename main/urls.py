from django.urls import path, include
from . import  views



urlpatterns = [
    path('', views.index ),
    path('registration', views.registration ),
    path('login', views.login ),
    path('search', views.search ),
    path('graphic', views.graphic ),
    path('salary', views.salary ),
    path('workbook', views.workbook ),
    path('pension', views.pension ),
    path('resetpassword', views.resetpassword ),
]
