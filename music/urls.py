from django.conf.urls import patterns, url
from .views import AlbumListView, AlbumCreateView, AlbumUpdateView


urlpatterns = []

# Album URLs
urlpatterns += patterns('',
    url(
        regex='^album/$',
        view=AlbumListView.as_view(),
        name='album_list'
    ),
    url(
        regex='^album/create/$',
        view=AlbumCreateView.as_view(),
        name='album_create',
    ),
    url(
        regex='^album/(?P<pk>\d+)/update/$',
        view=AlbumUpdateView.as_view(),
        name='album_update'
    ),
)

