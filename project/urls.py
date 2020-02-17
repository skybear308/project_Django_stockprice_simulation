from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chart.urls')),
]

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url('^$', include('chart.urls')),
# ]