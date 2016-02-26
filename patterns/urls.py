from django.conf.urls import url
from patterns import views as patterns_views


urlpatterns = [
    url(r'^', patterns_views.index, name='index'),
]


