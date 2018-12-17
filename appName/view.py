from django.http import HttpResponse
from django.shortcuts import render
def hello (request):
    # print
    context = {}
    context['hello']=[1,2,3,4,5,6,7,8,9,10]
    return render(request,'hello.html',context)
