from django.db import models


# 网站分区选择表
class PartChoice(models.Model):
    part = models.CharField(max_length=30, verbose_name='网站分区')

    class Meta:
        db_table = 'part'
        verbose_name = "网站分区"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str("%s" % self.part)


# 网站分组选择表
class GroupChoice(models.Model):
    group_part = models.ForeignKey(PartChoice, on_delete=models.CASCADE)
    group = models.CharField(max_length=30, verbose_name='网站分组')

    class Meta:
        db_table = 'group'
        verbose_name = "网站分组"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str("%s" % self.group)


# 网站信息表
class Site(models.Model):
    site_group = models.ForeignKey(GroupChoice, on_delete=models.CASCADE)
    url = models.URLField(verbose_name='网站链接')
    title = models.CharField(max_length=50, verbose_name="网站标题")
    info = models.CharField(max_length=200, blank=True, null=True, verbose_name="网站介绍")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        db_table = 'site'
        verbose_name = '网站信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
# null 是从数据库层面，允许为空，如果null==True的话，Django 在数据库中会将空值(empty)存储为 NULL，用SQL来说明就是为该列添加了NOT NULL的约束。默认是False。
# blank 是用于验证。如果一个字段的 blank=True ，Django 在进行表单数据验证时，会允许该字段是空值。如果字段的 blank=False ，该字段就是必填的。
