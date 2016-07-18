# coding:utf-8

from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
        自定义权限，只有创建者才能编辑
    """
    def has_objcet_permission(self, request, view, obj):
        # 所有人有读权限
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user









