from django.urls import path, include
from . import  views



urlpatterns = [
    path('mmenu', views.index ),
    path('', views.index ),
    path('registration', views.registration ),
    path('login', views.login ),
    path('search', views.search ),
    path('graphic', views.graphic ),
    path('salary', views.salary ),
    path('workbook', views.workbook ),
    path('pension', views.pension ),
    path('resetpassword', views.resetpassword ),
    path('stat_menu', views.stat_menu),
    path('stat_page', views.stat_pag1),
    path('page2', views.stat_pag2),
    path('page3', views.stat_pag3),
    path('page4', views.stat_pag4),

]
