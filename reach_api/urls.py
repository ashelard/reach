"""reach_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from reach_api import views
from django.conf.urls import url

urlpatterns = (
    # 计数器接口
    url(r'^api/count(/)?$', views.counter),

    url(r'^current/time(/)?$', views.get_current_time),
    url(r'^test/job(/)?$', views.test_job),
    url(r'^test/spider(/)?$', views.test_spider),
    url(r'^api/message/add(/)?$', views.add_wb_message),

    url(r'^api/ruler/spider_auth/get_by_name(/)?$', views.get_spider_auth_by_name),
    url(r'^api/ruler/spider_auth/add(/)?$', views.add_spider_auth),
    url(r'^api/ruler/spider_auth/update(/)?$', views.update_spider_auth_cookie),
    # 获取主页
    url(r'(/)?$', views.index),
)
