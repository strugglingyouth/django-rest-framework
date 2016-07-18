# coding:utf-8

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippet.models import Snippet
from snippet.serializers import SnippetSerializer



#class JSONResponse(HttpResponse):
    #"""
        #用于返回 JSON 数据
    #"""
    #def __init__(self, data, **kwargs):
        #content = JSONRenderer().render(data)
        #kwargs['content_type'] = 'application/json'
        #super(JSONResponse, self).__init__(content, **kwargs)


@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    """
        展示所有的 snippet 或者新创建的 snippet
        request.data 可以处理 JSON 和其他数据类型
        Response 对象可以根据客户端发出的请求来返回正确的数据类型（例如：浏览器请求返回html，使用命令行则返回json）
        formate 用于处理单一的数据格式后缀
    """

    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    """
        修改或删除一个 snippet
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



        












