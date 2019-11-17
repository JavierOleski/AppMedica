from django.core.files.storage import default_storage, FileSystemStorage
from django.db.models.fields.files import FieldFile
from django.shortcuts import render, redirect
from .forms import FichaForm
from .models import Ficha

class FakeField(object):
    storage = default_storage

fieldfile = FieldFile(None, FakeField, "dummy.txt")


def home(request):
    return render(request, 'home.html')


def acercade(request):
    return render(request, 'acercade.html')


def lista_pacientes(request):
    lista = Ficha.objects.all()
    return render(request, 'lista_pacientes.html', {
        'lista': lista
    })


def ficha(request):
    if request.method == 'POST':
        form = FichaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = FichaForm()
    return render(request, 'ficha.html', {
        'form': form
    })
