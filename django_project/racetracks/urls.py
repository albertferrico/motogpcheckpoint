from django.conf.urls import url
from .views import(
        RacetrackList,
        RacetrackDetail,
        RacetrackNew,
        RacetrackUpdated,
        RacetrackDelete,
)
urlpatterns = [
        url(r'^$', RacetrackList.as_view(), name='list'),
        url(r'^(?P<slug>[\w-]+)/$', RacetrackDetail.as_view(), name='detail'),
        url(r'^new$', RacetrackNew.as_view(), name='new'),
        url(r'^edit/(?P<pk>\d+)$', RacetrackUpdated.as_view(), name='edit'),
        url(r'^delete/(?P<pk>\d+)$', RacetrackDelete.as_view(), name='delete'),
]
