from django.conf.urls import url

from .views import(
        RiderList,
        RiderDetail,
        RiderNew,
        RiderUpdated,
        RiderDelete
)

urlpatterns = [
        url(r'^$', RiderList.as_view(), name='list'),
        url(r'^(?P<slug>[\w-]+)/$', RiderDetail.as_view(), name='detail'),
        url(r'^new$', RiderNew.as_view(), name='new'),
        url(r'^edit/(?P<pk>\d+)$', RiderUpdated.as_view(), name='edit'),
        url(r'^delete/(?P<pk>\d+)$', RiderDelete.as_view(), name='delete'),

]
