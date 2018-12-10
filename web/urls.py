from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from web import views
router = SimpleRouter()
router.register('item', views.WebView)
urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^list/(\d*)', views.list, name='list'),
    url(r'^look_art/(\d+)', views.look_art, name='look_art'),
]
urlpatterns += router.urls




