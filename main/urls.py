from django.urls import path
from . import  views



urlpatterns = [
    path('mmenu', views.index ),
    path('', views.index ),
    path('stat_menu', views.stat_menu),
    path('stat_page', views.stat_pag1),
    path('page2', views.stat_pag2),
    path('page3', views.stat_pag3),
    path('page4', views.stat_pag4),
    path('ras_menu',views.ras_menu),
    path('page5', views.stat_pag5),
    path('page6', views.stat_pag6),
    path('stat_menu2', views.stat_menu2),
    path('page7', views.stat_pag7),

]
