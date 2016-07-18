# coding:utf-8

from rest_framework import generics
from snippet.models import Snippet
from snippet.serializers import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SnippetList(generics.ListCreateAPIView):
    """
        展示所有的 snippet 或者新创建的 snippet
        generics.ListCeateAPIView 提供了 get，post，create，list 等方法 
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
    def perform_create(self, serializer):
        """
            perform_create() 这个
            方法准许我们修改实例如何被保存、处理任何由request或requested URL传递进来
            的隐含数据
        """
        serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        修改或删除一个 snippet
        generics.RetrieveUpdateDestroyAPIView 提供了 delete,get, patch, put 等方法
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
