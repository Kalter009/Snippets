from django.db import models

<<<<<<< HEAD
LANGS = (('py', 'Python'),
         ('js', 'JavaScript'),
         ('cpp', 'C++')
=======
LANGS = (
    ('py', "Python"),
    ('js', "JavaScript"),
    ('cpp', "C++")
>>>>>>> 10d881cfea7757b8123e3dc4ad917e71f9e69438
)

class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30, choices=LANGS)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(auto_now=True)
