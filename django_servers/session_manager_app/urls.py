"""session_manager_app urls."""

from django.urls import path
from django.contrib import admin
from django.contrib import admin
#from django.conf.urls import include, url
#from django.conf.urls.defaults import *



from session_manager_app import views

###from .views import MarkersMainView
###from .views import AveriasForm, AveriasCreate, AveriasUpdate, AveriasDelete

app_name = "session_manager_app"


urlpatterns = [
    path('', views.home, name='home'),
    path("create", views.create_telescop_parameters, name="telescop_parameters_create"),
    path("remove_items", views.remove_items, name="remove_items"),
    path('febe', views.febe, name='febe'),
    path("create_febe", views.create_febe_parameters, name="febe_parameters_create"),
    path("remove_febe_items", views.remove_febe_items, name="remove_feve_items"),
    path("upload_febe_items", views.upload_febe_items, name="update_feve_items"),
    #path('sources', views.sources, name='sources'),
    #path("create_sources", views.create_sources_parameters, name="sources_parameters_create"),

]



"""
""dashweb urls.""

from django.urls import path

from .views import MarkersMapView

from dashweb import views


from django.contrib import admin
#from django.conf.urls import include, url
#from django.conf.urls.defaults import *

from .views import AveriasForm, AveriasCreate, AveriasUpdate, AveriasDelete


app_name = "dashweb"


urlpatterns = [
    path('', views.home, name='home'),
    path("map/", AveriasCreate.as_view()),
    path('averias/', views.averias, name='averias'),

    #path("averias/create", AveriasCreate.as_view(), name="averias_create"),
    #path("create", AveriasCreate.as_view(), name="averias_create"),
    path("averias/create", views.averias, name="averias_create"),
    path("create", views.averias, name="averias_create"),

    path("averias/update/<int:pk>/", AveriasUpdate.as_view(), name="averias_update"),
    path("averias/delete/<int:pk>/", AveriasDelete.as_view(), name="averias_delete"),
    path("averias/delete", AveriasDelete.as_view(), name="averias_delete"),
    path("averias/remove_items", views.remove_items, name="remove_items"),
    path("remove_items", views.remove_items, name="remove_items"),
    path("averias/update_items", views.update_items, name="update_items"),

    # Aquí es donde se redirecciona cuando se borra un registro:
    #path("averias/", AveriasView.as_view(), name="averias_list")
    #path("averias/", AveriasForm.as_view(), name="averias_list")

    #url(r'^averias/create/$', views.AveriasCreate.as_view(), name='averias_create'),
    #url(r'^averias/(?P<pk>\d+)/update/$', views.AveriasUpdate.as_view(), name='averias_update'),
    #url(r'^averias/(?P<pk>\d+)/delete/$', views.AveriasDelete.as_view(), name='averias_delete'),


]

"""



