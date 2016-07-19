# coding:utf-8


from rest_framework import serializers
from snippet.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
        snippets和用户是一种反向关联，默认情况下不会包含
        在 ModelSerializer 类
    """
    snippet = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    class Meta:
        model = User
        fields = ('url', 'username', 'snippet')


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    """
        使用 ModelSerializer 类，类似于 ModelForm 类
        自动检测字段
        简单定义了 create() 和 update() 方法
    """
    # source 决定了显示user的哪个参数值，并且可以 使用user的任何属性
    # ReadOnlyField 只读属性，序列化的时候展示，反序列化的时候不会被修改
    # 也可以使用 CharField(read_only=True) 来替代它
    # owner = serializers.ReadOnlyField(source='owner.username')
    owner = serializers.CharField(read_only=True, source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    class Meta:
        model = Snippet
        fields = ('url', 'highlight', 'title', 'code', 'linenos', 'language', 'style', 'owner')














