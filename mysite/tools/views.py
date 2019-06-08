from django.shortcuts import render, get_object_or_404
from .models import Item, TypeItem

def hss(request):
    broca = Item.objects.filter(type=1)
    tipo = TypeItem.objects.get(pk=1)
    template_name = 'tools/tabela.html'
    context = {
        'broca': broca,
        'tipo': tipo
    }
    return render(request, template_name, context)

def metalDuro(request):
    tipo = TypeItem.objects.get(pk=2)
    broca = Item.objects.filter(type_id=2).order_by('diameter',)
    template_name = 'tools/tabela.html'
    context = {
        'tipo': tipo,
        'broca': broca
    }
    return render(request, template_name, context)

