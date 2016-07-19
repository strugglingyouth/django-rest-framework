# coding:utf-8

from rest_framework import permissions
from snippet.models import Snippet
from snippet.serializers import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User
from snippet.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
        viewsets 自动提供 list（） 和 detail（） 方法
        ReadOnlyMoldeViewSet 提供只读的方法 
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SnippetViewSet(viewsets.ModelViewSet):
    """
        viewset 提供 list`, `create`, `retrieve` `update` and `destroy` 方法
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # 确保了只有认证用户才有读写权限，未认证用户则只有只读权限
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )

    # 使用 detail_route 来创建自定义的动作
    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        """
            perform_create() 这个
            方法准许我们修改实例如何被保存、处理任何由request或requested URL传递进来
            的隐含数据
        """
        serializer.save(owner=self.request.user)
    





#@api_view(['GET'])
#def api_root(request, format=None):
    #"""
        #使用 reverse 函数返回完全限定的 url
    #"""
    #return Response({
        #'users': reverse('user-list', request=request, format=format),
        #'snippets': reverse('snippet-list', request=request, format=format)
    #})





