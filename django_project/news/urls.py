from django.conf.urls import url

from .views import(
        NewsList,
        NewsNew,
        NewsUpdated,
        NewsDelete
)

urlpatterns = [
        url(r'^$', NewsList.as_view(), name='list'),
        url(r'^new$', NewsNew.as_view(), name='new'),
        url(r'^edit/(?P<pk>\d+)$', NewsUpdated.as_view(), name='edit'),
        url(r'^delete/(?P<pk>\d+)$', NewsDelete.as_view(), name='delete'),
]
