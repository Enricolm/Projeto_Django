from django.shortcuts import render
# Create your views here.

def view (r):
    return render(r ,'galeria/index.html')

def view2 (r):
    return render(r,'galeria/imagem.html')

