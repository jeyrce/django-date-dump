# -*- coding: utf-8 -*-
__author__ = 'eamil@lujianxin.cn'
__time__ = '18-12-26 下午10:28'
__popurse__ = """这个文件的作用：
    自定义权限
"""

from rest_framework.permissions import BasePermission


class AlwaysRefuse(BasePermission):
    """总是无权限"""

    def has_object_permission(self, request, view, obj):
        return False

    def has_permission(self, request, view):
        return False


if __name__ == '__main__':
    pass
