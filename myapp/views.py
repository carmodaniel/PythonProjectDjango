from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'mensagem': 'Esta é a página inicial do meu aplicativo Django.'}
    return render(request, 'myapp/index.html', context)
