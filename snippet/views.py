# coding:utf-8

from rest_framework import generics
from snippet.models import Snippet
from snippet.serializers import SnippetSerializer


class SnippetList(generics.ListCreateAPIView):
    """
        展示所有的 snippet 或者新创建的 snippet
        generics.ListCeateAPIView 提供了 get，post，create，list 等方法 
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        修改或删除一个 snippet
        generics.RetrieveUpdateDestroyAPIView 提供了 delete,get, patch, put 等方法
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
