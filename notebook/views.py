from django.shortcuts import render
from .models import Notebook

def index(request):
    notebooks = Notebook.objects.all()
    context = {'notebooks': notebooks}
    return render(request, 'notebook/index.html', context)
