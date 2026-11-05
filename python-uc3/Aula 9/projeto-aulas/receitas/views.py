from django.shortcuts import render

# receitas/views.py

from django.shortcuts import get_object_or_404, render

from .models import Receita


def lista_receitas(request):
    """Exibe todas as receitas publicadas, das mais recentes para as mais antigas."""

    receitas = Receita.objects.filter(publicada=True)

    context = {
        "receitas": receitas,
    }

    return render(request, "receitas/lista.html", context)


def detalhe_receita(request, pk):
    """
    Exibe os detalhes de uma receita específica.

    O parâmetro 'pk' vem da URL dinâmica:
    /receita/<int:pk>/
    """

    # Busca a receita pelo ID e exige que ela esteja publicada.
    # Se não existir, o Django retorna automaticamente um erro 404.
    receita = get_object_or_404(
        Receita,
        pk=pk,
        publicada=True,
    )

    context = {
        "receita": receita,
    }

    return render(request, "receitas/detalhe.html", context)