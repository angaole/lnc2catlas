# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class snp(models.Model):
    number = models.IntegerField(primary_key=True)
    lncrnaid = models.CharField(max_length=34)
    snpid = models.CharField(max_length=34)
    isld = models.BooleanField(default=False)
    snplocation = models.CharField(max_length=34)
    score = models.CharField(max_length=34)
    disease = models.CharField(max_length=34)

class protein(models.Model):
    number = models.IntegerField(primary_key=True)
    lncrnaid = models.CharField(max_length=34)
    proteinname = models.CharField(max_length=34)
    proteintranscript = models.BooleanField(default=False)
    protein_url = models.CharField(max_length=34)
    score = models.CharField(max_length=34)
    disease = models.CharField(max_length=34)

class lncrna(models.Model):
    lncrnaid = models.CharField(max_length=34, primary_key=True)
    location = models.CharField(max_length=34)
    strand = models.CharField(max_length=3)
    classs = models.CharField(max_length=20)
    length = models.CharField(max_length=5)
    exons = models.CharField(max_length=2)
    alias = models.CharField(max_length=500)
    pmid = models.CharField(max_length=500)
    expression = models.CharField(max_length=1000)
    sequence = models.TextField()
