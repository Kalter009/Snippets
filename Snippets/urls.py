from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.index_page),
    path('snippets/add', views.add_snippet_page, name='add_snippet'),
    path('snippets/list', views.snippets_page, name='snippets_list'),
    path('snippets/<int:snippet_id>', views.snippet_details, name='snippet_details'),
=======
    path('', views.index_page, name='home'),
    path('snippets/add', views.add_snippet_page, name='snippets-add'),
    path('snippets/list', views.snippets_page, name='snippets-list'),
    path('snippet/<int:snippet_id>', views.snippet_detail, name='snippet-detail'),
    path('snippet/<int:snippet_id>/delete', views.snippet_delete, name='snippet-delete'),
    path('snippet/<int:snippet_id>/edit', views.snippet_edit, name='snippet-edit'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
