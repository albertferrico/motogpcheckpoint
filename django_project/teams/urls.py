from django.conf.urls import url

from .views import(
        TeamList,
        TeamDetail,
        TeamNew,
        TeamUpdated,
        TeamDelete
)

urlpatterns = [
        url(r'^$', TeamList.as_view(), name='list'),
        url(r'^(?P<slug>[\w-]+)/$', TeamDetail.as_view(), name='detail'),
        url(r'^nuevo$', TeamNew.as_view(), name='new'),
        url(r'^edit/(?P<pk>\d+)$', TeamUpdated.as_view(), name='edit'),
        url(r'^delete/(?P<pk>\d+)$', TeamDelete.as_view(), name='delete'),
]
