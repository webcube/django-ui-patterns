try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url

from .views import PatternCategoryView, PatternDetailView, IndexView

urlpatterns = patterns(
    '',
    url(
        r'^group/(?P<category>.*)/$',
        PatternCategoryView.as_view(),
        name="category"
    ),
    url(r'^(?P<slug>.*)/$', PatternDetailView.as_view(), name="detail"),
    url(r'^$', IndexView.as_view(), name="index"),
)
