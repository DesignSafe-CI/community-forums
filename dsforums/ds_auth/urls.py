from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

urlpatterns = patterns(
    'ds_auth.views',
    url(r'^$', 'login_options', name='login'),
    url(r'^logged-out/$', 'logged_out', name='logout'),
    url(r'^agave/$', 'agave_oauth', name='agave_oauth'),
    url(r'^agave/callback/$', 'agave_oauth_callback', name='agave_oauth_callback'),
    url(r'^agave/session-error/$', 'agave_session_error', name='agave_session_error'),
)
