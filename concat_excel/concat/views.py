from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
import os
import time
import random


def handle(filePath):

    filename = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    paths = os.listdir(filePath)

    data = pd.read_excel(filePath + paths[0])

    for i in range(1, len(paths)):
        thisdata = pd.read_excel(filePath + paths[i])
        data = data.append(thisdata, ignore_index=True)

    data.to_excel(filePath + filename + '.xlsx', index=False)

    return filename + '.xlsx'


def delete(filePath, exfile):

    filenames = os.listdir(filePath)

    try:
        for thisname in filenames:
            if thisname != exfile:
                os.remove(filePath + thisname)
    except Exception as ex:
        print("清空文件夹时发生异常：%s" % ex)


def upload_file(request):

    filePath = 'C:/web/concat_django/excels/'
    # filePath = 'E:/web/'
    datename = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())) + '_' + str(random.randint(0,1000))

    os.makedirs(filePath + datename)
    filePath = filePath + datename + '/'

    if request.method == "POST":    # 请求方法为POST时，进行处理
        files = request.FILES.getlist('excels')
        for f in files:
            destination = open(filePath + f.name, 'wb+')
            for chunk in f.chunks():
                destination.write(chunk)
            destination.close()

    res = handle(filePath)
    delete(filePath, res)
    print(filePath + res)

    response = HttpResponse(open(filePath + res, 'rb'), content_type ='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=' + res

    return response