from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index, name="dashboard_home"),
	url(r'^signin$', views.signin, name="dashboard_signin"),
	url(r'^login$', views.login, name="dashboard_login"),
	url(r'^register$', views.register, name="dashboard_register"),
	url(r'^create$', views.create, name="dashboard_create"),
	url(r'^dashboard$', views.dashboard, name="dashboard_dashboard"),
	url(r'^dashboard/new$', views.new, name="dashboard_new"),
	url(r'^dashboard/edit/(?P<id>\d+)$', views.edit, name="dashboard_edit"),
	url(r'^dashboard/destroy/(?P<id>\d+)$', views.destroy, name="dashboard_destroy"),
	url(r'^dashboard/update/(?P<id>\d+)$', views.update, name="dashboard_update"),
	url(r'^dashboard/show/(?P<id>\d+)$', views.show, name="dashboard_show"),
	url(r'^dashboard/post/(?P<id>\d+)$', views.post, name="dashboard_post"),
	url(r'^dashboard/reply/(?P<id>\d+)$', views.reply, name="dashboard_reply"),
	url(r'^dashboard/profile$', views.profile, name="dashboard_profile"),
	url(r'^logoff$', views.logoff, name="dashboard_logoff")
]