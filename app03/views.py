# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect

user_info = {
    'zhang': {'pwd': "123123"},
    'neng': {'pwd': "147258"},
}
def login(request):
    if request.method == "GET":
        return render(request, 'app03login.html')
    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('pwd')
        dic = user_info.get(u)
        if not dic:
            return render(request, 'app03login.html')
        if dic['pwd'] == p:
            res = redirect('/app03index/')
            # res.set_cookie('username111',u,max_age=10)
            # import datetime
            # current_date = datetime.datetime.utcnow()
            # current_date = current_date + datetime.timedelta(seconds=5)
            # res.set_cookie('username111',u,expires=current_date)
            res.set_cookie('mycookice_k',u)
            # res.set_cookie('user_type',"asdfjalskdjf",httponly=True)
            return res
        else:
            return render(request, 'app03login.html')


def index(request):
    v = request.COOKIES.get('mycookice')
    if v:
        return render(request, 'app03index.html', {'current_user': v})
    else:
        return redirect('/app03login/')