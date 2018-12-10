from django.conf.urls import url, include
# from django.contrib import admin
urlpatterns = [
    url(r'web/', include('web.urls', namespace='web')),
    url(r'admin/', include('back_web.urls', namespace='admin'))
]
