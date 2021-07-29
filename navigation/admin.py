from django.contrib import admin
from .models import PartChoice, GroupChoice, Site
from import_export.admin import ImportExportModelAdmin
from .resource import SiteResource


class SiteAdmin(ImportExportModelAdmin):
    resource_class = SiteResource
    list_display = ('site_group', 'title', 'url', 'info')
    search_fields = ['title', 'info']
    list_filter = ['title', 'info']
    list_per_page = 20


admin.site.register(PartChoice)
admin.site.register(GroupChoice)
admin.site.register(Site, SiteAdmin)
