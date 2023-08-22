<<<<<<< HEAD
from django.forms import ModelForm
=======
from django.forms import ModelForm, Textarea, TextInput
>>>>>>> 10d881cfea7757b8123e3dc4ad917e71f9e69438
from MainApp.models import Snippet


class SnippetForm(ModelForm):
   class Meta:
<<<<<<< HEAD
       model = Snippet
       # Описываем поля, которые будем заполнять в форме
       fields = ['name', 'lang', 'code']
=======
        model = Snippet
        # Описываем поля, которые будем заполнять в форме
        fields = ['name', 'lang', 'code']
        labels = {'name': '', 'lang': '', 'code': ''}
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Название сниппета'}),
            'code': Textarea(attrs={'placeholder': 'Код сниппета'}),
        }
  

>>>>>>> 10d881cfea7757b8123e3dc4ad917e71f9e69438
