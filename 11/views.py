from django.shortcuts import HttpResponse, render
def index(request):
    return HttpResponse("<h1>a view funcionou fi<h1>")
def sobre(request):
    return HttpResponse("<h1>sobre o sistema<h1>")
def contato(request):
    return HttpResponse("<h1>esta é a página de contato fi<h1>")
def ajuda(request):
    return HttpResponse("<h1>esta é a página de ajuda<h1>")

    