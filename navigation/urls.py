from django.urls import path
from . import views

app_name = 'navigation'
urlpatterns = [
    # path 路径后面要加/ 与1.x的区别
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('pm', views.pm, name='pm'),
    path('ui', views.ui, name='ui'),
    path('cehua', views.cehua, name='cehua'),
    path('blog', views.blog, name='blog'),
    # path('articles/<year>/<month>/', views.month_archive),
    # path('articles/<year>/<month>/<int:pk>/', views.article_detail),
]




