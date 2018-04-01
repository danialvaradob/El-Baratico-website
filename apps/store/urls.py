from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
	url(r'^login/$', auth_views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    path('<int:producto_id>/', views.DetailView.as_view(), name='detail'),

]




