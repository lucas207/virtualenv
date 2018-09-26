from django.shortcuts import render, redirect
from django_tables2 import RequestConfig
from django.core.files import File
from django.urls import reverse
from .models import Messages
from .tables import MessagesTable
import logging, os

# Create your views here.
def home(request):
    print('go upload file')
    #open file location
    file = open('./readcsv/csv/outrasmsg.csv')
    data = file.read()
    print(data)

    table = MessagesTable(Messages.objects.all())
    RequestConfig(request).configure(table)
    return render(request, './table.html', {'table': table, 'dinamic': data})

# def upload(request):
#     print('go upload file')
#     #open file location
#     file = open('./readcsv/csv/outrasmsg.csv')
#     data = file.read()
#     print(data)
#     print(request.user)
#     # request.user.message_set.create(dinamic = data)
#     # file = File.open('csv/teste2-relatorios.csv')

#     table = MessagesTable(Messages.objects.all())
#     RequestConfig(request).configure(table)
#     return render(request, './table.html', {'table': table, 'dinamic': data})