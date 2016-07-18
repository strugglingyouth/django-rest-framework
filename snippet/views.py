# coding:utf-8

from rest_framework import mixins
from rest_framework import generics
from snippet.models import Snippet
from snippet.serializers import SnippetSerializer


class SnippetList(mixins.ListModelMixin, 
                  mixins.CreateModelMixin, 
                  generics.GenericAPIView):
    """
        展示所有的 snippet 或者新创建的 snippet
        mixin类则提供了 .list() 和 .ctreae() 的行为
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SnippetDetail(mixins.RetrieveModelMixin, 
                    mixins.UpdateModelMixin, 
                    mixins.DestroyModelMixin, 
                    generics.GenericAPIView):
    """
        修改或删除一个 snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs) 


