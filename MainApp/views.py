from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib import auth


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)

@login_required
def add_snippet_page(request):
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
            snippet = form.save(commit=False)
            if request.user.is_authenticated:
                snippet.user = request.user
                snippet.save()
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
    try:
        snippet = Snippet.objects.get(id=snippet_id)
    except ObjectDoesNotExist:
        raise Http404
    context = {
        'pagename': 'Просмотр сниппета',
        'snippet': snippet,
        'type': 'view'
        }
    return render(request, 'pages/snippet_detail.html', context)


def snippet_delete(request, snippet_id):
    snippet = Snippet.objects.get(id=snippet_id)
    snippet.delete()
    # Перенаправление на ту страницу, с которой пришел
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

def snippet_edit(request, snippet_id):
    try:
        snippet = Snippet.objects.get(id=snippet_id)
    except ObjectDoesNotExist:
        raise Http404
    # Хотим получить страницу данных сниппета
    if request.method == "GET":
        context = {
            'pagename': 'Редактирование сниппета',
            'snippet': snippet,
            'type': 'edit'
        }
        return render(request, 'pages/snippet_detail.html', context)
    
    # Хотим создать новый Сниппет(данные от формы)
    if request.method == "POST":
        data_form = request.POST
        snippet.name = data_form["name"]
        snippet.lang = data_form["lang"]
        snippet.code = data_form["code"]
        snippet.creation_date = data_form["creation_date"]
        snippet.save()
        return redirect("snippets-list")


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            context = {
                'pagename': 'PythonBin',
                'errors': ['wrong username or password']
            }
            return render(request, 'pages/index.html', context)
    return redirect('home')


def logout(request):
    auth.logout(request)
    return redirect(request.META.get("HTTP_REFERER", '/'))

# def create_snippet(request):
#     if request.method == "POST":
#         form = SnippetForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("snippets-list")
#         return render(request,'add_snippet.html', {'form': form})
