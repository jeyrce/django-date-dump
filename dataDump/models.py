# -*- coding: utf-8 -*-
__author__ = 'eamil@lujianxin.cn'
__time__ = '18-12-26 下午10:15'
__popurse__ = """这个文件的作用：
    数据模型
"""

from django.db import models


class Goods(models.Model):
    """商品表"""
    code = models.CharField(max_length=11, primary_key=True, verbose_name='条码')
    name = models.CharField(max_length=32, unique=True, verbose_name='名称')
    base_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, verbose_name='指导价格')
    add = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        verbose_name_plural = verbose_name = '商品'
        db_table = 'goods'

    def __str__(self):
        return self.name


class Order(models.Model):
    """订单表"""
    number = models.CharField(max_length=32, null=True, blank=True, primary_key=True, verbose_name='单号')
    goods = models.ManyToManyField(Goods, related_name='goodses', verbose_name='包含商品')
    add = models.DateTimeField(auto_now_add=True, verbose_name='生单时间')
    total_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='总价')
    payment = models.CharField(max_length=6, default='支付宝免密')

    class Meta:
        verbose_name_plural = verbose_name = '订单'
        db_table = 'order'

    def __str__(self):
        return self.number


if __name__ == '__main__':
    pass
