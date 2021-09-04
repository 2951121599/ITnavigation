from django.contrib import admin
from .models import PartChoice, GroupChoice, Site
from import_export.admin import ImportExportModelAdmin
from .resource import SiteResource


# 网站分组
class GroupAdmin(ImportExportModelAdmin):
    resource_class = SiteResource
    # list_display = ('group', 'group_part', 'get_part')
    # list_display = ('group', 'group_part')
    list_display = ('group_part', 'group')
    search_fields = ['group']
    list_filter = ['group_part__part', ]
    # list_display_links =('group', )
    list_editable = ('group', )
    list_per_page = 20

    # def get_part(self, obj):
    #     return '%s' % obj.group_part.part
    #
    # get_part.short_description = '网站分区'


# 网站信息
class SiteAdmin(ImportExportModelAdmin):
    resource_class = SiteResource  # 导入导出
    # list_display = ('site_group', 'title', 'url', 'info', 'get_part')
    list_display = ('site_group', 'title', 'url', 'info')
    search_fields = ['title', 'info']
    list_filter = ['title', 'info']
    list_editable = ('title', 'info')
    list_per_page = 20

    # def get_part(self, obj):
    #     return '%s' % obj.site_group.group_part.part + '-' + obj.site_group.group
    #
    # get_part.short_description = '网站分区'


admin.site.register(PartChoice)
admin.site.register(GroupChoice, GroupAdmin)
admin.site.register(Site, SiteAdmin)
# admin.site.register(Site)
