from django.shortcuts import render

def index(request):
    return render(request,"main/index.html")
def stat_menu(request):
    return render(request,'main/stat_menu.html')
def stat_pag1(request):
    return render(request,'main/stat_page.html')
def stat_pag2(request):
    return render(request,'main/page2.html')
def stat_pag3(request):
    return render(request,'main/page3.html')
def stat_pag4(request):
    return render(request,'main/page4.html')
def ras_menu(request):
    return render(request,'main/ras_menu.html')
def stat_pag5(request):
    return render(request,'main/page5.html')
def stat_pag6(request):
    return render(request,'main/page6.html')
def stat_menu2(request):
    return render(request,'main/stat_menu2.html')
def stat_pag7(request):
    return render(request,'main/page7.html')
