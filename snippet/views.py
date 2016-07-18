# coding:utf-8

from rest_framework import generics
from rest_framework import permissions
from snippet.models import Snippet
from snippet.serializers import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User
from snippet.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers


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
    # 确保了只有认证用户才有读写权限，未认证用户则只有只读权限
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
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
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )



@api_view(['GET'])
def api_root(request, format=None):
    """
        使用 reverse 函数返回完全限定的 url
    """
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })


class SnippetHighlight(generics.GenericAPIView):
    """
        创建语法高亮视图
    """
    queryset = Snippet.objects.all()
    renderers_classes = (renderers.StaticHTMLRenderer, )

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)








