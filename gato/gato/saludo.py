from django.shortcuts import render

def saludo(request):
    return render(request, 'gato/saludo.html')