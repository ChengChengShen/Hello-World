# -*- coding:utf-8 -*-
from . import models
from django.shortcuts import render
from django.http import HttpResponse

def testdb(request):
    # test1 = t_user(name='w3cshcool.cn!')
    # test1.save()
    test_list = list(models.t_user.objects.all())
    test_list_toarr = []
    # print(test_list_toarr)
    for item in test_list:
        json = {}
        json['id'] = item.id
        json['name'] = item.name
        test_list_toarr.append(json)
    return render(request,'testdb.html',{'test_list_toarr':test_list_toarr})

