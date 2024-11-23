from django.shortcuts import render

def index(request):
    return render(request,"main/index.html")
def registration(request):
    return render(request,"main/registration.html")
def login(request):
    return render(request,"main/login.html")
def search(request):
    return render(request,"main/search.html")
def graphic(request):
    return render(request,"main/graphic.html")
def salary(request):
    return render(request,"main/salary.html")
def workbook(request):
    return render(request,"main/workbook.html")
def pension(request):
    return render(request,"main/pension.html")
def resetpassword(request):
    return render(request,"main/resetpassword.html")
