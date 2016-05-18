"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.render_index, name='index'),
    url(r'^delete/(?P<item_name>.+)$', views.delete_item_and_refresh, name="delete_item"),
    url(r'^item/(?P<task_name>.+)/add$', views.add_item_and_refresh, name='add_item'),
    url(r'^task/add$', views.add_task_and_refresh, name='add_task'),
    # url(r'^add$', views.render_index, name='add_task'),
    # url(r'^submit$', views., name=''),
    # url(r'^task/(?P<task_id>.+)/submit$', views., name=''),
    # url(r'^task/(?P<task_id>.+)/delete$', views., name=''),
]
