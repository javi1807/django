from django.shortcuts import render
def herencia(request,name):
    context={'name':name}
    return render(request, 'herencia.html', context)

def ejemplo(request):
    return render (request, 'ejemplo.html', {})

def otra(request):
    return render(request, 'otra.html', {})

def index(request):
    return render(request, 'index.html', {})