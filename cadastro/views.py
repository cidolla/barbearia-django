from django.shortcuts import render

def pagina_login(request):
    return render(request, 'cadastro/login.html')

def pagina_barbearia(request):
    return render(request, 'cadastro/barbearia.html')