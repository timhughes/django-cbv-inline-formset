from django.urls import path, re_path
from .views import AlbumListView, AlbumCreateView, AlbumUpdateView


urlpatterns = []

# Album URLs
urlpatterns =[
    re_path(
        r'^album/$',
        view=AlbumListView.as_view(),
        name='album_list'
    ),
    re_path(
        r'^album/create/$',
        view=AlbumCreateView.as_view(),
        name='album_create',
    ),
    re_path(
        r'^album/(?P<pk>\d+)/update/$',
        view=AlbumUpdateView.as_view(),
        name='album_update'
    ),
]

