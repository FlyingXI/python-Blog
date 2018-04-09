# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from stock.models import Stock
import json
import tushare as ts

from django.http import HttpResponse

# Create your views here.


def get_stock(request):

    context = {}
    result = ts.get_stock_basics()
    print(result.shape)
    #result = result.head(2)
    stock_json = result.to_json(orient='records', force_ascii=False)

    stock_list = json.loads(stock_json)
    stock_object_list = []

    for i in stock_list:
        stock_object_list.append(Stock(i['name'], i['industry'], i['area'], i['pb'], i['pe']))

    context['all'] = stock_object_list

    return render(request, 'stock.html', context)

