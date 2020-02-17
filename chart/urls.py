from django.urls import path
# from django.conf.urls import url, include
from . import views

app_name = 'chart'

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
]

# urlpatterns = [
#     url('^$', views.IndexView.as_view(), name="index"),
# ]