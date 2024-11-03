import json
import logging
from datetime import datetime

import pytz
from django.http import JsonResponse
from django.shortcuts import render
from .models import Counters, SpiderAuth

logger = logging.getLogger('log')


def get_current_time(request, _):
    utc_now = datetime.now(pytz.utc)
    # 转换为东八区时间
    czone = pytz.timezone('Asia/Shanghai')
    now = utc_now.astimezone(czone)
    time = now.strftime("%Y-%m-%d %H:%M:%S")

    logger.info('get current time result: {}'.format(time))
    return JsonResponse({'code': 0, 'data': time},
                        json_dumps_params={'ensure_ascii': False})


def index(request, _):
    """
    获取主页

     `` request `` 请求对象
    """

    return render(request, 'index.html')


def counter(request, _):
    """
    获取当前计数

     `` request `` 请求对象
    """

    rsp = JsonResponse({'code': 0, 'errorMsg': ''}, json_dumps_params={'ensure_ascii': False})
    if request.method == 'GET' or request.method == 'get':
        rsp = get_count()
    elif request.method == 'POST' or request.method == 'post':
        rsp = update_count(request)
    else:
        rsp = JsonResponse({'code': -1, 'errorMsg': '请求方式错误'},
                           json_dumps_params={'ensure_ascii': False})
    logger.info('response result: {}'.format(rsp.content.decode('utf-8')))
    return rsp


def get_count():
    """
    获取当前计数
    """

    try:
        data = Counters.objects.get(id=1)
    except Counters.DoesNotExist:
        return JsonResponse({'code': 0, 'data': 0},
                            json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'code': 0, 'data': data.count},
                        json_dumps_params={'ensure_ascii': False})


def update_count(request):
    """
    更新计数，自增或者清零

    `` request `` 请求对象
    """

    logger.info('update_count req: {}'.format(request.body))

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    if 'action' not in body:
        return JsonResponse({'code': -1, 'errorMsg': '缺少action参数'},
                            json_dumps_params={'ensure_ascii': False})

    if body['action'] == 'inc':
        try:
            data = Counters.objects.get(id=1)
        except Counters.DoesNotExist:
            data = Counters()
        data.id = 1
        data.count += 1
        data.save()
        return JsonResponse({'code': 0, "data": data.count},
                            json_dumps_params={'ensure_ascii': False})
    elif body['action'] == 'clear':
        try:
            data = Counters.objects.get(id=1)
            data.delete()
        except Counters.DoesNotExist:
            logger.info('record not exist')
        return JsonResponse({'code': 0, 'data': 0},
                            json_dumps_params={'ensure_ascii': False})
    else:
        return JsonResponse({'code': -1, 'errorMsg': 'action参数错误'},
                            json_dumps_params={'ensure_ascii': False})


def get_spider_auth_by_name(request):
    name = request.GET.get('name')
    data = SpiderAuth.objects.get(name=name)
    return JsonResponse({'code': 0, 'data': data},
                        json_dumps_params={'ensure_ascii': False})


def add_spider_auth(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    auth = SpiderAuth()
    auth.name = body['name']
    auth.wid = body['wid']
    auth.wuid = body['wuid']
    auth.cookie = body['cookie']

    auth.save()

    return JsonResponse({'code': 0, 'data': 'success'},
                        json_dumps_params={'ensure_ascii': False})


def update_spider_auth_cookie(request):
    name = request.GET.get('name')
    wid = request.GET.get('wid')
    wuid = request.GET.get('wuid')
    cookie = request.GET.get('name')
    auth = None
    if name:
        auth = SpiderAuth.objects.get(name=name)
    elif wid:
        auth = SpiderAuth.objects.get(wid=wid)
    elif wuid:
        auth = SpiderAuth.objects.get(wuid=wuid)

    if not auth:
        return JsonResponse({'code': 0, 'data': 'not exist,can\'t update'},
                            json_dumps_params={'ensure_ascii': False})

    auth.cookie = cookie
    auth.save()

    return JsonResponse({'code': 0, 'data': auth},
                        json_dumps_params={'ensure_ascii': False})
