

from django.shortcuts import render, redirect
from .models import UsuarioSustentavel
from .forms import UsuarioForm
import matplotlib.pyplot as plt
import io
import urllib, base64
from django.shortcuts import render

def relatorio(request):
    return render(request, 'relatorio.html')


def calcular_grafico(usuario):
    labels = ['Energia', 'Água', 'Resíduos', 'Transporte']
    valores = [usuario.consumo_energia, usuario.consumo_agua, usuario.residuos, usuario.uso_transporte]

    fig, ax = plt.subplots()
    ax.bar(labels, valores, color=['blue', 'green', 'red', 'orange'])
    ax.set_ylabel('Consumo')
    ax.set_title('Consumo Sustentável')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    imagem_png = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    
    return imagem_png

def cadastro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'cadastro.html', {'form': form})

def lista_usuarios(request):
    usuarios = UsuarioSustentavel.objects.all()
    return render(request, 'lista.html', {'usuarios': usuarios})

def detalhes_usuario(request, id):
    usuario = UsuarioSustentavel.objects.get(id=id)
    grafico = calcular_grafico(usuario)
    return render(request, 'detalhes.html', {'usuario': usuario, 'grafico': grafico})
