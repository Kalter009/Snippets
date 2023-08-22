from django.http import Http404
from django.shortcuts import render, redirect
from MainApp import models
from MainApp.forms import SnippetForm

from MainApp.models import Snippet
from MainApp.forms import SnippetForm


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
<<<<<<< HEAD
    if request.method == "GET":
        form = SnippetForm()
        context = {'pagename': 'Добавление нового сниппета',
                   'form': form
                   }
        return render(request, 'pages/add_snippet.html', context)
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect("view_snippets")
        return render(request, 'pages/add_snippet.html', {'form': form})


def snippets_page(request):
    context = {'pagename': 'Просмотр сниппетов',
               'snippets': models.Snippet.objects.all()
               }
    return render(request, 'pages/view_snippets.html', context)

def snippet_details(request, snippet_id):
    snippet = models.Snippet.objects.get(id=snippet_id)
    pagename = snippet.name
    context = {'pagename': pagename,
               'snippet': snippet
               }
    return render(request, 'pages/snippet_details.html', context)

def add_snippet_page(request):
   form = SnippetForm()
   return render(request, 'pages/add_snippet.html', {'form': form})
=======
    # Хотим получить чистую форму для заполнения
    if request.method == "GET":
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': form
        }
        return render(request, 'pages/add_snippet.html', context)
    
    # Хотим создать новый Сниппет(данные от формы)
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("snippets-list")
        return render(request,'pages/add_snippet.html', {'form': form})

def snippets_page(request):
    snippets = Snippet.objects.all()
    context = {
        'pagename': 'Просмотр сниппетов',
        'snippets': snippets
        }
    return render(request, 'pages/view_snippets.html', context)


def snippet_detail(request, snippet_id):
    snippet = Snippet.objects.get(id=snippet_id)
    context = {
        'pagename': 'Просмотр сниппета',
        'snippet': snippet
        }
    return render(request, 'pages/snippet_detail.html', context)


# def create_snippet(request):
#     if request.method == "POST":
#         form = SnippetForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("snippets-list")
#         return render(request,'add_snippet.html', {'form': form})
>>>>>>> 10d881cfea7757b8123e3dc4ad917e71f9e69438
