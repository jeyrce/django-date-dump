# -*- coding: utf-8 -*-
__author__ = 'eamil@lujianxin.cn'
__time__ = '18-12-26 下午10:30'
__popurse__ = """这个文件的作用：
    测试接口
"""

"""
    导出订单列表  lujianxin   2018-12-06
"""
from .excel import DataDumpView
from .models import Order
from rest_framework.permissions import IsAuthenticated


class OrderDumpExample(DataDumpView):
    """导出订单"""
    model = Order  # 要下载的表
    fields = '__all__'  # 要导出的字段
    method_fields = {'detail': '订单详情'}  # 获取这个值需要自己实现get__sign方法
    exclude = []  # 导出时排除的字段
    order_field = 'id'  # 排序依据，必须指定
    limit = 200  # 当不重构get_queryset方法时返回的记录条数
    sheet_size = 30  # 每个sheet的记录条数，默认是300
    file_name = '订单报表'  # 最终生成的文件名:订单报表.xls
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self, request):
        """一般来说需要重写这个方法指定要下载的文件记录"""
        return super().get_queryset(request)

    def get__sign(self, obj):
        """上面我们在mehtod_fields里面定义了{'sign': '签名'}
        因此我们实现get_sign方法，这个方法的返回值将作为每条记录对应字段的值
        如果这个字段表里面也有，那么将会覆盖表里面
        """
        return '测试签名'


class OrderDumpView(DataDumpView):
    """导出订单详情"""
    model = OrderInfo
    fields = '__all__'
    method_fields = {'detail': '订单详情'}
    exclude = []
    order_field = 'trade_date'
    sheet_size = 500
    file_name = '订单报表'
    permission_classes = []

    def get_queryset(self, request):
        """从request中获取参数进行筛选"""
        return super().get_queryset(request)

    def get__detail(self, obj):
        # 这个方法写双划线, 为了和我基础类中的方法区分开
        import json
        from orders.models import OrderDetails
        details = OrderDetails.objects.filter(order_id_id=obj.id)
        goodses = []
        for detail in details:
            goods = {
                '订单': detail.order_id.number,
                '商品': detail.goods_id.goods_name,
                '数量': detail.goods_num,
                '价格': detail.goods_price.__str__(),
                '促销价': detail.goods_super.__str__()
            }
            goodses.append(goods)
        return str(goodses)


order_dump_out = OrderDumpView.as_view()

if __name__ == '__main__':
    pass
