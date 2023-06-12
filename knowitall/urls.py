from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('building/<int:pk>', views.BuildingDetailView.as_view(), name='building-detail'),
    path('buildings/', views.BuildingListView.as_view(), name='buildings'),
    path('block/<int:pk>', views.BlockDetailView.as_view(), name='block-detail'),
    path('blocks/',  views.BlockListView.as_view(), name='blocks'),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('subsystem/<int:pk>', views.SubsystemDetailView.as_view(), name='subsystem-detail'),
    path('subsystems/', views.SubsystemListView.as_view(), name='subsystems'),
    path('function/<int:pk>', views.FunctionDetailView.as_view(), name='function-detail'),
    path('functions/', views.FunctionListView.as_view(), name='functions'),
    path('location/<int:pk>', views.LocationDetailView.as_view(), name='location-detail'),
    path('locations/', views.LocationListView.as_view(), name='locations'),
    path('rack/<int:pk>', views.RackDetailView.as_view(), name='rack-detail'),
    path('racks/', views.RackListView.as_view(), name='racks'),
    path('pts/<int:pk>', views.PTSDetailView.as_view(), name='pts-detail'),
    path('ptss/', views.PTSListView.as_view(), name='ptss'),
    path('software/<int:pk>', views.SoftwareDetailView.as_view(), name='software-detail'),
    path('softwares/', views.SoftwareListView.as_view(), name='softwares'),
]

# Add URLConf to create, update, and delete

urlpatterns += [
    path('building/create/', views.BuildingCreate.as_view(), name='building-create'),
    path('building/<int:pk>/update/', views.BuildingUpdate.as_view(), name='building-update'),
    path('building/<int:pk>/delete/', views.BuildingDelete.as_view(), name='building-delete'),
    path('block/create/', views.BlockCreate.as_view(), name='block-create'),
    path('block/<int:pk>/update/', views.BlockUpdate.as_view(), name='block-update'),
    path('block/<int:pk>/delete/', views.BlockDelete.as_view(), name='block-delete'),
    path('project/create/', views.ProjectCreate.as_view(), name='project-create'),
    path('project/<int:pk>/update/', views.ProjectUpdate.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', views.ProjectDelete.as_view(), name='project-delete'),
    path('subsystem/create/', views.SubsystemCreate.as_view(), name='subsystem-create'),
    path('subsystem/<int:pk>/update/', views.SubsystemUpdate.as_view(), name='subsystem-update'),
    path('subsystem/<int:pk>/delete/', views.SubsystemDelete.as_view(), name='subsystem-delete'),
    path('function/create/', views.FunctionCreate.as_view(), name='function-create'),
    path('function/<int:pk>/update/', views.FunctionUpdate.as_view(), name='function-update'),
    path('function/<int:pk>/delete/', views.FunctionDelete.as_view(), name='function-delete'),
    path('location/create/', views.LocationCreate.as_view(), name='location-create'),
    path('location/<int:pk>/update/', views.LocationUpdate.as_view(), name='location-update'),
    path('location/<int:pk>/delete/', views.LocationDelete.as_view(), name='location-delete'),
    path('rack/create/', views.RackCreate.as_view(), name='rack-create'),
    path('rack/<int:pk>/update/', views.RackUpdate.as_view(), name='rack-update'),
    path('rack/<int:pk>/delete/', views.RackDelete.as_view(), name='rack-delete'),
    path('pts/create/', views.PTSCreate.as_view(), name='pts-create'),
    path('pts/<int:pk>/update/', views.PTSUpdate.as_view(), name='pts-update'),
    path('pts/<int:pk>/delete/',  views.PTSDelete.as_view(), name='pts-delete'),
    path('software/create/', views.SoftwareCreate.as_view(), name='software-create'),
    path('software/<int:pk>/update/', views.SoftwareUpdate.as_view(), name='software-update'),
    path('software/<int:pk>/delete/', views.SoftwareDelete.as_view(), name='software-delete'),
]
