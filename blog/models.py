# Serve para adicionar pedaços de arquivos, enxutando o código

from django.conf import settings
from django.db import models
from django.utils import timezone

# Define o Modelo, é um Objeto

class Post(models.Model): # models.Model -  o Post é um modelo de Django, então deve ser salvo no BD
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # link para outro modelo
    title = models.CharField(max_length=200) # texto com caracteres limitados
    text = models.TextField() # este campo é para textos sem um limite fixo
    created_date = models.DateTimeField(default=timezone.now) #  este é para data e hora
    published_date = models.DateTimeField(blank=True, null=True) #  este é para data e hora

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self): # quando chamar __str__(), obterá um texto (string) com o título do Post
        return self.title