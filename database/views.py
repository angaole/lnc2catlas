# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from database.models import snp
from database.models import protein
from database.models import lncrna
# Create your views here.
def search(request):
    return render_to_response('search.html')

def searchby(request, conten):
    content = str(conten)
    if content=="":
        return render_to_response('search.html')
    elif content.find("!")!=-1 or content.find("@")!=-1!=-1 or content.find("$")!=-1 or content.find("%")!=-1 or content.find("^")!=-1 or content.find("*")!=-1 or content.find(",")!=-1 or content.find("/")!=-1:
        return render_to_response('search_error.html')
    else:
        flag = 0
        if len(content)>3 and content[0:4]="ENST":
            flag = 1
            lists1 = lncrna.objects.filter(Q(lncrnaid__icontains=content))
            if len(lists1)==1:
                result(bala)
            else:
                lists1 = snp.objects.filter(Q(snpid__icontains=content))
                if len(lists1)==0:
                    return render_to_response('search_none.html')
                if len(lists1)>10:
                    p = Paginator(lists1, 10)
                    page = request.GET.get('page')
                    page = str(page)
                    print page
                    try:
                        lists = p.page(page)
                    except PageNotAnInteger:
                        page = "1"
                        lists = p.page(1)
                    except EmptyPage:
                        page = str(p.num_pages)
                        lists = p.page(p.num_pages)
                    num_pages = p.num_pages
                    print "num_pages", num_pages
                    asa = []
                    if int(page)>3 and int(page)<num_pages-2:
                        asa = ["1", str(int(page)-2), str(int(page)-1), page, str(int(page)+1), str(int(page)+2), str(num_pages)]
                    if page=="1":
                        asa = ["1", "2", "3", str(num_pages)]
                    if page=="2":
                        asa = ["1", "2", "3", "4", str(num_pages)]
                    if page=="3":
                        asa = ["1", "2", "3", "4", "5", str(num_pages)]
                    if page==str(num_pages):
                        asa = [1, num_pages-2, num_pages-1, num_pages]
                    if page==str(num_pages-1):
                        asa = [1, num_pages-3, num_pages-2, num_pages-1, num_pages]
                    if page==str(num_pages-2):
                        asa = [1, num_pages-4, num_pages-3, num_pages-2, num_pages-1, num_pages]
                    print asa
                    c = {"lists":lists, "asa":asa, "contents":content}
                    return render(request, 'result_snp.html', c)
                if len(lists1)<10 and len(lists1)>0:
                    c = {"lists":lists1, "contents":content}
                    return render_to_response('result_single_snp.html', c)

                lists2 = protein.objects.filter(Q(proteintranscript__icontains=content))
                if len(lists2)==0:
                    return render_to_response('search_none.html')
                if len(lists2)>20:
                    p = Paginator(lists2, 20)
                    page = request.GET.get('page')
                    page = str(page)
                    print page
                    try:
                        lists = p.page(page)
                    except PageNotAnInteger:
                        page = "1"
                        lists = p.page(1)
                    except EmptyPage:
                        page = str(p.num_pages)
                        lists = p.page(p.num_pages)
                    num_pages = p.num_pages
                    print "num_pages", num_pages
                    asa = []
                    if int(page)>3 and int(page)<num_pages-2:
                        asa = ["1", str(int(page)-2), str(int(page)-1), page, str(int(page)+1), str(int(page)+2), str(num_pages)]
                    if page=="1":
                        asa = ["1", "2", "3", str(num_pages)]
                    if page=="2":
                        asa = ["1", "2", "3", "4", str(num_pages)]
                    if page=="3":
                        asa = ["1", "2", "3", "4", "5", str(num_pages)]
                    if page==str(num_pages):
                        asa = [1, num_pages-2, num_pages-1, num_pages]
                    if page==str(num_pages-1):
                        asa = [1, num_pages-3, num_pages-2, num_pages-1, num_pages]
                    if page==str(num_pages-2):
                        asa = [1, num_pages-4, num_pages-3, num_pages-2, num_pages-1, num_pages]
                    print asa
                    c = {"lists":lists, "asa":asa, "contents":content}
                    return render(request, 'result_protein.html', c)
                if len(lists1)<20 and len(lists1)>0:
                    c = {"lists":lists1, "contents":content}
                    return render_to_response('result_single_protein.html', c)
        if len(content)>1 and content[0:2]="rs":
            flag = 2
            lists1 = snp.objects.filter(Q(snpid__icontains=content))
            if len(lists1)==0:
                return render_to_response('search_none.html')
            if len(lists1)>20:
                p = Paginator(lists1, 20)
                page = request.GET.get('page')
                page = str(page)
                print page
                try:
                    lists = p.page(page)
                except PageNotAnInteger:
                    page = "1"
                    lists = p.page(1)
                except EmptyPage:
                    page = str(p.num_pages)
                    lists = p.page(p.num_pages)
                num_pages = p.num_pages
                print "num_pages", num_pages
                asa = []
                if int(page)>3 and int(page)<num_pages-2:
                    asa = ["1", str(int(page)-2), str(int(page)-1), page, str(int(page)+1), str(int(page)+2), str(num_pages)]
                if page=="1":
                    asa = ["1", "2", "3", str(num_pages)]
                if page=="2":
                    asa = ["1", "2", "3", "4", str(num_pages)]
                if page=="3":
                    asa = ["1", "2", "3", "4", "5", str(num_pages)]
                if page==str(num_pages):
                    asa = [1, num_pages-2, num_pages-1, num_pages]
                if page==str(num_pages-1):
                    asa = [1, num_pages-3, num_pages-2, num_pages-1, num_pages]
                if page==str(num_pages-2):
                    asa = [1, num_pages-4, num_pages-3, num_pages-2, num_pages-1, num_pages]
                print asa
                c = {"lists":lists, "asa":asa, "contents":content}
                return render(request, 'result_snp.html', c)
            if len(lists1)<20 and len(lists1)>0:
                c = {"lists":lists1, "contents":content}
                return render_to_response('result_single_snp.html', c)
        if flag==0:
            lists1 = protein.objects.filter(Q(proteintranscript__icontains=content))
            if len(lists1)==0:
                return render_to_response('search_none.html')
            if len(lists1)>20:
                p = Paginator(lists1, 20)
                page = request.GET.get('page')
                page = str(page)
                print page
                try:
                    lists = p.page(page)
                except PageNotAnInteger:
                    page = "1"
                    lists = p.page(1)
                except EmptyPage:
                    page = str(p.num_pages)
                    lists = p.page(p.num_pages)
                num_pages = p.num_pages
                print "num_pages", num_pages
                asa = []
                if int(page)>3 and int(page)<num_pages-2:
                    asa = ["1", str(int(page)-2), str(int(page)-1), page, str(int(page)+1), str(int(page)+2), str(num_pages)]
                if page=="1":
                    asa = ["1", "2", "3", str(num_pages)]
                if page=="2":
                    asa = ["1", "2", "3", "4", str(num_pages)]
                if page=="3":
                    asa = ["1", "2", "3", "4", "5", str(num_pages)]
                if page==str(num_pages):
                    asa = [1, num_pages-2, num_pages-1, num_pages]
                if page==str(num_pages-1):
                    asa = [1, num_pages-3, num_pages-2, num_pages-1, num_pages]
                if page==str(num_pages-2):
                    asa = [1, num_pages-4, num_pages-3, num_pages-2, num_pages-1, num_pages]
                print asa
                c = {"lists":lists, "asa":asa, "contents":content}
                return render(request, 'result_protein.html', c)
            if len(lists1)<20 and len(lists1)>0:
                c = {"lists":lists1, "contents":content}
                return render_to_response('result_single_protein.html', c)

def searchfor(request, dise):
    

def result(request, ids):
    if request.method=="POST":
        lists = lncrna.objects.filter(lncrnaid=ids)
        for line in lists:
            strs = line.expression
        list_expression = strs.split()
        list_expression = [float(i) for i in list_expression]
        list_snp = snp.objects.filter(lncrnaid=ids)
        list_protein = protein.objects.filter(lncrnaid=ids)
        c = {"lists":lists, "list_snp":list_snp, "list_protein":list_protein, "list_expression":list_expression}
        return render_to_response('detail.html', c)

def home(request):
    return render_to_response('home.html')

def browse(request, a, b):
    return render_to_response('browse.html')

def download(request):
    return render_to_response('download.html')

def help(request):
    return render_to_response('help.html')

def test(request):
    return render_to_response('test.html')

def data(request):
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment;filename=All-Data.txt'
    full_path = "all-data"
    if os.path.exists(full_path):
        response['Content-Length'] = os.path.getsize(full_path)
        content = open(full_path, 'rb').read()
        response.write(content)
        return response
    else:
        return HttpResponse(u'cannot find the file')

def saveexpre(request, ids):
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment;filename='+ids+'_gene.zip'
    list0 = seqe.objects.filter(ids=ids)
    for line in list0:
        strs = line.expre
    list_expre = strs.split()
    f = open("downfile/file", 'w')
    f.write(list_expre)
    f.close()
    full_path = "downfile/file"
    response['Content-Length'] = os.path.getsize(full_path)
    content = open(full_path, 'rb').read()
    response.write(content)
    os.system("rm downfile/file")
    return response

def savesnp(request, ids):
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment;filename='+ids+'_gene.txt'
    list_gen = genes.objects.filter(lncrnaid=ids)
    f = open("downfile/file", 'w')
    for i in list_gen:
        f.write(i.snpid+"\t"+i.isld+"\t"+i.score+"\t"+i.disease+"\n")
    f.close()
    full_path = "downfile/file"
    response['Content-Length'] = os.path.getsize(full_path)
    content = open(full_path, 'rb').read()
    response.write(content)
    os.system("rm downfile/file")
    return response

def saveprotein(request, ids):
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment;filename='+ids+'_disease.txt'
    lists = messa.objects.filter(lncrnaid=ids)
    f = open("downfile/file", 'w')
    for i in lists:
        f.write(i.proteinname+"\t"+proteintranscript+"\t"+i.score+"\t"+i.disease+"\n")
    f.close()
    full_path = "downfile/file"
    response['Content-Length'] = os.path.getsize(full_path)
    content = open(full_path, 'rb').read()
    response.write(content)
    os.system("rm downfile/file")
    return response

def showpicsnp(request, ids, snpid):
    return render_to_response('help.html')

def showpicpro(request, ids, proteintranscript):
    return render_to_response('help.html')
