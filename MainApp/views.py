from django.http import Http404
from django.shortcuts import render, redirect
from MainApp import models
from MainApp.forms import SnippetForm


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
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
