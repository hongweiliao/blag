from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from back_web import views

router = SimpleRouter()
router.register('user', views.User)

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^index/', views.index, name='index'),
    url(r'^article/', views.article, name='art'),
    url(r'^category/', views.category, name='cate'),
    url(r'^addarticle', views.add_article, name='add_art'),
    url(r'^deleteart/(\d+)', views.delete_art, name='delete_art'),
    url(r'^updateart/(\d+)', views.update_art, name='update_art'),
    url(r'^updatecat/(\d+)', views.update_cat, name='update_cat'),
    url(r'^deletecat/(\d+)', views.delete_cat, name='delete_cat'),
    url(r'^manageuser/', views.manage_user)

]
urlpatterns += router.urls
