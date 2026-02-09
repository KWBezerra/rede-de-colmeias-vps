from django.db import models

# Create your models here.

class Tutorial(models.Model):
    title = models.CharField('titulo', max_length=200)
    slug = models.SlugField('slug', unique=True, help_text='URL amigavel')
    content_md = models.TextField('Conteudo em markdown')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tutorial'
        verbose_name_plural = 'Tutoriais'
        ordering = ['title']

    def __str__(self):
        return self.title