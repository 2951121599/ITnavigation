# -*-coding:utf-8-*- 
# 作者：   cts
# 文件名:  resource.py
# 当前系统日期时间：2021/6/25，22:15
from import_export import resources
from import_export.fields import Field
from .models import Site


class SiteResource(resources.ModelResource):
    class Meta:
        model = Site
        exclude = ['id']  # 排除的字段
        # fields = ('part', 'group')  # 指定哪些字段需要导入
        export_order = ('part', 'group')  # 导出的字段顺序
        import_id_fields = ['url']  # 设置导入主键字段
        # title = Field(attribute='title', column_name='网站标题')
        widgets = {
            'add_time': {'format': '%Y.%m.%d'},
        }
