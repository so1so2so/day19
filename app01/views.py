# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse

# Create your views here.



def login(requst,nid):
    # print requst.POST.getlist('like')
    # return render(requst, 'login.html')
    return HttpResponse(nid)
# USER_DICT = {
#     '1': {'name': 'root1', 'email': 'root1@live.com'},
#     '2': {'name': 'root2', 'email': 'root2@live.com'},
#     '3': {'name': 'root3', 'email': 'root3@live.com'},
#     '4': {'name': 'root4', 'email': 'root4@live.com'},
#     '5': {'name': 'root5', 'email': 'root5@live.com'},
# }
def index(request):
    # nid = request.GET.get('nid')
    if request.method == "GET":
        USER_DICT = models.host.objects.filter(nid__gt=0).values('ip','b__caption','hostname','port')
        print USER_DICT
        return render(request, 'index.html', {'detail_info': USER_DICT})
    elif request.method == "POST":
    # detail_info = USER_DICT[nid]
        u = request.POST.get('name')
        p = request.POST.get('pwd')
        models.host.objects.create(username=u,passwd=p)
    return redirect("/index")


def detail(request, nid):
    if request.method == "GET":
        USER = models.pymysql.objects.filter(id =nid)

        return render(request, 'detail.html', {'detail': USER})
    # nid = request.GET.get('nid')

    # return HttpResponse(nid)

from app01 import models


def orm(request):
    # models.pymysql.objects.create(
    #     username = "root",
    #     passwd = "123456",
    # )
    # dic ={
    #     'username':"zhang2",
    #     'passwd' :"neng2",
    # }
    # obj =models.pymysql(
    #    **dic
    # )
    # obj.save()
    res= models.pymysql.objects.all()
    # for i in res:
        # print i.id, i.username, i.passwd

    return render(request, 'orm.html',)
def host(request):
    # v1 = models.Host.objects.filter(nid__gt=0)
    # return render(request, 'host.html', {'v1': v1})
    if request.method == "GET":
        v1 = models.host.objects.filter(nid__gt=0)
        v2 = models.host.objects.filter(nid__gt=0).values('nid', 'hostname', 'b_id',
                                                          'b__caption')
        v3 = models.host.objects.filter(nid__gt=0).values_list('nid', 'hostname',
                                                               'b_id','b__caption')
        b_list = models.business.objects.all()
        return render(request, 'index.html', {'v1': v1, 'v2': v2,
                                         'v3': v3, 'v4': b_list})
    elif request.method == "POST":
        h = request.POST.get('hostname')
        ip = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        models.host.objects.create(hostname=h, ip=ip, port=p,
                                   b_id =b)
        return redirect('/host')


def test_ajax(request):
    print request.method, request.GET.get('user'), request.GET.get('pwd')
    return HttpResponse('ajax关门')