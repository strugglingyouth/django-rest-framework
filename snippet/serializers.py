# coding:utf-8


from rest_framework import serializers
from snippet.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
    """
        序列化，反序列化字段
    """
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True,max_length=100)
    code = serializers.CharField(style={'base_template':'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    
    def create(self, validated_data):
        """
            数据合法就创建并返回一个 snippet 实例
        """
        return Snippet.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        """
            数据合法并存在时则更新数据
        """
        
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)

        instance.save()   # 保存实例
        return instance






