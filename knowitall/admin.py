from django.contrib import admin
from .models import Building, Block, Project, Subsystem, Function, Location, Rack, Rack_TYPE, Interface, PTS, PTS_TYPE, Software, Software_TYPE, PTS_SF, PTS_INT, PTS_RACK, PTS_FUNC, SUBS_FUNC
# Register your models here.
admin.site.register(Building)
admin.site.register(Block)
admin.site.register(Project)
admin.site.register(Subsystem)
admin.site.register(Function)
admin.site.register(Location)
admin.site.register(Rack)
admin.site.register(Rack_TYPE)
admin.site.register(Interface)
admin.site.register(PTS)
admin.site.register(PTS_TYPE)
admin.site.register(Software)
admin.site.register(Software_TYPE)
admin.site.register(PTS_SF)
admin.site.register(PTS_INT)
admin.site.register(PTS_RACK)
admin.site.register(PTS_FUNC)
admin.site.register(SUBS_FUNC)

class Building_Admin(admin.ModelAdmin):
    list_display = ('Building_code','Building_name')
    fields = ['Building_code','Building_name']
    """Administration object for models.
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields),
       grouping the date fields horizontally
    """
class Block_Admin(admin.ModelAdmin):
    list_display = ('Block_name','Block_number')
    fields = ['Block_name','Block_number']
class Project_Admin(admin.ModelAdmin):
    list_display = ('Project_name','Project_def')
    fields = ['Project_name','Project_def']
class Subsystem_Admin(admin.ModelAdmin):
    list_display = ('Subsystem_name','Subsystem_def')
    fields = ['Subsystem_name','Subsystem_def']
class Function_Admin(admin.ModelAdmin):
    list_display = ('Function_name','Function_def')
    fields = ['Function_name','Function_def']
class Location_Admin(admin.ModelAdmin):
    list_display = ('Location_name','Location_code')
    fields = ['Location_name','Location_code']
class Rack_Admin(admin.ModelAdmin):
    list_display = ('Rack_name','Rack_KKS')
    fields = ['Rack_name','Rack_KKS']
class Rack_TYPE_Admin(admin.ModelAdmin):
    list_display = ('Rack_TYPE_name','Rack_TYPE_def')
    fields = ['Rack_TYPE_name','Rack_TYPE_def']
class Interface_Admin(admin.ModelAdmin):
    list_display = ('Interface_name','Interface_def')
    fields = ['Interface_name','Interface_def']
class PTS_admin(admin.ModelAdmin):
    list_display = ('PTS_name','PTS_code', 'PTS_code', 'PTS_interface')
    fields = ['PTS_name','PTS_code', 'PTS_code', 'PTS_interface']
class PTS_TYPE_Admin(admin.ModelAdmin): 
    list_display = ('PTS_TYPE_name','PTS_TYPE_def')
    fields = ['PTS_TYPE_name','PTS_TYPE_def']
class Software_Admin(admin.ModelAdmin):
    list_display = ('name','version','type')
    fields = ['Software_name','Software_version','Software_type']
class Software_TYPE_Admin(admin.ModelAdmin):
    list_display = ('Subsystem','Function')
    fields = ['Subsystem','Function']
class PTS_SF_Admin(admin.ModelAdmin):
    list_display = ('PTS','Software')
    fields = ['PTS','Software']
class PTS_INT_Admin(admin.ModelAdmin):
    list_display = ('PTS','Interface')
    fields = ['PTS','Interface']
class PTS_RACK_Admin(admin.ModelAdmin):
    list_display = ('Rack','PTS')
    fields = ['Rack','PTS']
class PTS_FUNC_Admin(admin.ModelAdmin):
    list_display = ('PTS','Function')
    fields = ['PTS','Function']
class SUBS_FUNC(admin.ModelAdmin):
    list_display = ('Subsystem','Function')
    fields = ['Subsystem','Function']
