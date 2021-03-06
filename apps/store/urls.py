from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    url(r'^home.html$', views.product_list, name='product_list'),
    url(r'^delete_all_cart_items/$', views.delete_all_cart_items, name='delete_all_cart_items'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}, name='logout'),
    url(r'^carrito_detalle/$', views.carrito_detalle, name='carrito_detalle'),
    path(r'^agregar_producto/(<int:producto_id>)/$', views.agregar_producto, name='agregar_producto'),
    path(r'^delete_cart_item/(<int:producto_id>)/', views.delete_cart_item, name='delete_cart_item'),
    path('<int:producto_id>/', views.detail, name='detail'),
    path('<int:producto_id>/', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<category_slug>[-\w]+)/$',views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),

]

    
