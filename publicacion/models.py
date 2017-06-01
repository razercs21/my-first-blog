# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre= models.CharField(max_length=150)


class Autor(models.Model):
    nombre= models.CharField(max_length=150)
    edad= models.IntegerField()

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    nombre= models.CharField(max_length=150)
    autor= models.ForeignKey(Autor,related_name="autores")
    categorias= models.ManyToManyField(Categoria)