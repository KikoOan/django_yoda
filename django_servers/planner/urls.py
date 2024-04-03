"""planner urls."""

from django.urls import path
from django.contrib import admin
#from django.conf.urls import include, url
#from django.conf.urls.defaults import *



from planner import views

app_name = "planner"


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path("create_session", views.create_session, name="create_session"),
    path("remove_session", views.remove_session, name="remove_session"),
    path("upload_session", views.upload_session, name="upload_session"),
    path("json_file", views.json_file, name="json_file"),
    #path("macro_file", views.macro_file, name="macro_file"),


    path("admin_febes", views.admin_febes, name="admin_febes"),
    path("create_configurated_febe", views.create_configurated_febe, name="create_configurated_febe"),
    path("remove_admin_febe", views.remove_admin_febe, name="remove_admin_febe"),
    path("upload_admin_febe", views.upload_admin_febe, name="upload_admin_febe"),
    path("update_configurated_febe", views.update_configurated_febe, name="update_configurated_febe"),





    path("add_febe1", views.add_febe1, name="add_febe1"),
    path("add_febe", views.add_febe, name="add_febe"),
    path("create_febe", views.create_febe, name="create_febe"),
    path("remove_febe", views.remove_febe, name="remove_febe"),
    path("upload_febe", views.upload_febe, name="upload_febe"),
    path("update_febe", views.update_febe, name="update_febe"),


    path("add_source", views.add_source, name="add_source"),
    path("create_source", views.create_source, name="create_source"),
    path("remove_source", views.remove_source, name="remove_source"),
    path("upload_source", views.upload_source, name="upload_source"),
    path("update_source", views.update_source, name="update_source"),

    path("add_setup", views.add_setup, name="add_ssetup"),
    path("create_setup", views.create_setup, name="create_setup"),
    path("remove_setup", views.remove_setup, name="remove_setup"),
    path("upload_setup", views.upload_setup, name="upload_setup"),
    path("update_setup", views.update_setup, name="update_setup"),

    path("add_integrations", views.add_integrations, name="add_integrations"),
    path("create_integrations", views.create_integrations, name="create_integrations"),
    path("remove_integrations", views.remove_integrations, name="remove_integrations"),
    path("upload_integrations", views.upload_integrations, name="upload_integrations"),
    path("update_integrations", views.update_integrations, name="update_integrations"),


    path("add_cal", views.add_cal, name="add_cal"),
    path("create_cal", views.create_cal, name="create_cal"), 
    path("remove_cal", views.remove_cal, name="remove_cal"),
    path("upload_cal", views.upload_cal, name="upload_cal"),
    path("update_cal", views.update_cal, name="update_cal"),


    path("add_aim", views.add_aim, name="add_aim"),
    path("create_aim", views.create_aim, name="create_aim"), 
    path("remove_aim", views.remove_aim, name="remove_aim"),
    path("upload_aim", views.upload_aim, name="upload_aim"),
    path("update_aim", views.update_aim, name="update_aim"),


    path("add_foc", views.add_foc, name="add_foc"),
    path("create_foc", views.create_foc, name="create_foc"), 
    path("remove_foc", views.remove_foc, name="remove_foc"),
    path("upload_foc", views.upload_foc, name="upload_foc"),
    path("update_foc", views.update_foc, name="update_foc"),






    #path("create_sources", views.create_sources, name="create_sources"),
    #path("create_setup", views.create_setup, name="create_setup"),
    #path("create_integration", views.create_integration, name="create_integration"),
    #path("session_complete", views.session_complete, name="session_complete"),
    #path("create", views.create_telescop_parameters, name="telescop_parameters_create"),
    #path("remove_items", views.remove_items, name="remove_items"),
    #path('febe', views.febe, name='febe'),
    #path("create_febe", views.create_febe_parameters, name="febe_parameters_create"),
    #path("remove_febe_items", views.remove_febe_items, name="remove_feve_items"),
    #path("upload_febe_items", views.upload_febe_items, name="update_feve_items"),
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



