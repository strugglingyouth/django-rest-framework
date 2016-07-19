# coding:utf-8

"""snippets URL Configuration

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
from django.conf.urls import url, include 
from rest_framework.urlpatterns import format_suffix_patterns
from snippet import views
from snippet.views import SnippetViewSet, UserViewSet
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})


#router = DefaultRouter()
#router.register(r'snippets', views.SnippetViewSet)
#router.register(r'users', views.UserViewSet)



#urlpatterns = [
    #url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

#]

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^snippets/(?P<pk>\d+)/highlight/$', snippet_highlight, name='snippet-highlight'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>\d+)/$', user_detail, name='user-detail'),
    url(r'^snippets/$', snippet_list, name='snippet-list'),
    url(r'^snippets/(?P<pk>\d+)/$', snippet_detail, name='snippet-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

#登录功能
urlpatterns += [
   url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    ]

