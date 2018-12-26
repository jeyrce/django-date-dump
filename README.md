# django-date-dump
基于djang，rest_framework的通用数据导出接口

### 依赖

- django2.x
- rest_framework3.x
- XlsxWriter>=1.1.2
- xlwt>=1.3.0

### 快速开始

- 下载依赖

```
git clone https://github.com/ixser/django-date-dump.git
cd <你的项目>
pip install -r requirements.txt
```

- 导入类编写drf接口

```
from excel import DataDumpView

class OrderDump(DataDumpView)
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
```

- 配置接口路由

```
from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('order-dump', views.OrderDumpView, base_name='order-dump')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]

```

- 修改settings配置

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'django_filters',
    'dataDump',
]
...
# 数据库改成自己的连接
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

- 运行项目即可

### 注意：　

- 接口默认GET请求。
- 必须指定permission_class，即使设为空列表
- 下载的文件为xls格式，每次请求最好在url添加时间戳或者随机数，否则每次都会从缓存中读取。