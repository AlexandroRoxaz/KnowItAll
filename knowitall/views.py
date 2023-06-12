from django.shortcuts import render

# Create your views here.

from .models import Building, Block, Project, Subsystem, Function, Location, Rack, PTS, Software 

def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_buildings = Building.objects.all().count()
    num_blocks = Block.objects.all().count()
    num_projects = Project.objects.all().count()
    num_subsystems = Subsystem.objects.all().count()
    num_functions = Function.objects.all().count()
    num_locations = Location.objects.all().count()
    num_racks = Rack.objects.all().count()
    num_pts = PTS.objects.all().count()
    num_software = Software.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits+1



    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_buildings': num_buildings, 'num_blocks': num_blocks, 'num_projects': num_projects, 'num_subsystems': num_subsystems, 'num_functions': num_functions, 'num_locations': num_locations, 'num_racks': num_racks, 'num_pts': num_pts, 'num_software': num_software},
    )
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
     
class BuildingListView(LoginRequiredMixin, generic.ListView):
    model = Building
    paginate_by = 10

class BuildingDetailView(LoginRequiredMixin, generic.DetailView):
    model = Building

class BlockListView(LoginRequiredMixin, generic.ListView):
    model = Block
    paginate_by = 10

class BlockDetailView(LoginRequiredMixin, generic.DetailView):
    model = Block

class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    paginate_by = 10

class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project

class SubsystemListView(LoginRequiredMixin, generic.ListView):
    model = Subsystem
    paginate_by = 10

class SubsystemDetailView(LoginRequiredMixin, generic.DetailView):
    model = Subsystem

class FunctionListView(LoginRequiredMixin, generic.ListView):
    model = Function
    paginate_by = 10

class FunctionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Function

class LocationListView(LoginRequiredMixin, generic.ListView):
    model = Location
    paginate_by = 10

class LocationDetailView(LoginRequiredMixin, generic.DetailView):
    model = Location    

class RackListView(LoginRequiredMixin, generic.ListView):
    model = Rack    
    paginate_by = 10

class RackDetailView(LoginRequiredMixin, generic.DetailView):
    model = Rack

class PTSListView(LoginRequiredMixin, generic.ListView):
    model = PTS
    paginate_by = 10

class PTSDetailView(LoginRequiredMixin, generic.DetailView):
    model = PTS

class SoftwareListView(LoginRequiredMixin, generic.ListView):
    model = Software
    paginate_by = 10

class SoftwareDetailView(LoginRequiredMixin, generic.DetailView):
    model = Software    

class BuildingCreate(LoginRequiredMixin, CreateView):
    model = Building
    fields = ['Building_name','Building_code']
class BuildingUpdate(LoginRequiredMixin, UpdateView):
    model = Building
    fields = '__all__' # Not recommended (potential security issue if more fields added)
class BuildingDelete(LoginRequiredMixin, DeleteView):
    model = Building
    success_url = reverse_lazy('buildings')
class BlockCreate(LoginRequiredMixin, CreateView):
    model = Block
    fields = ['Block_name','Block_number']
class BlockUpdate(LoginRequiredMixin, UpdateView):
    model = Block
    fields = '__all__' # Not recommended (potential security issue if more fields added)
class BlockDelete(LoginRequiredMixin, DeleteView):
    model = Block
    success_url = reverse_lazy('blocks')
class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['Project_name','Project_def']
class ProjectUpdate(LoginRequiredMixin, UpdateView):
    model = Project
    fields = '__all__' # Not recommended (potential security issue if more fields added)
class ProjectDelete(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('projects')
class SubsystemCreate(LoginRequiredMixin, CreateView):
    model = Subsystem
    fields = ['Subsystem_name', 'Subsystem_def', 'Subsystem_project', 'Subsystem_block']
class SubsystemUpdate(LoginRequiredMixin, UpdateView):
    model = Subsystem
    fields = '__all__' # Not recommended (potential security issue if more fields added)
class SubsystemDelete(LoginRequiredMixin, DeleteView):
    model = Subsystem
    success_url = reverse_lazy('subsystems')
class FunctionCreate(LoginRequiredMixin, CreateView):
    model = Function
    fields = ['Function_name', 'Function_def']
class FunctionUpdate(LoginRequiredMixin, UpdateView):
    model = Function
    fields = '__all__' # Not recommended (potential security issue if more fields added)
class FunctionDelete(LoginRequiredMixin, DeleteView):
    model = Function
    success_url = reverse_lazy('functionss')
class LocationCreate(LoginRequiredMixin, CreateView):
    model = Location
    fields = ['Location_name', 'Location_code', 'Location_building']
class LocationUpdate(LoginRequiredMixin, UpdateView):
    model = Location
    fields = '__all__' # Not recommended (potential security issue if more fields added)
class LocationDelete(LoginRequiredMixin, DeleteView):
    model = Location
    success_url = reverse_lazy('locations')
class RackCreate(LoginRequiredMixin, CreateView):
    model = Rack
    fields = ['Rack_name', 'Rack_KKS', 'Rack_location', 'Rack_type']
class RackUpdate(LoginRequiredMixin, UpdateView):
    model = Rack
    fields = '__all__' # Not recommended (potential security issue if more fields added)    
class RackDelete(LoginRequiredMixin, DeleteView):
    model = Rack
    success_url = reverse_lazy('racks')
class PTSCreate(LoginRequiredMixin, CreateView):
    model = PTS
    fields = ['PTS_name', 'PTS_code', 'PTS_type']
class PTSUpdate(LoginRequiredMixin, UpdateView):
    model = PTS
    fields = '__all__' # Not recommended (potential security issue if more fields added)
class PTSDelete(LoginRequiredMixin, DeleteView):
    model = PTS
    success_url = reverse_lazy('ptss')
class SoftwareCreate(LoginRequiredMixin, CreateView):
    model = Software
    fields = ['Software_name', 'Software_version', 'Software_type']
class SoftwareUpdate(LoginRequiredMixin, UpdateView):
    model = Software
    fields = '__all__' # Not recommended (potential security issue if more fields added)
class SoftwareDelete(LoginRequiredMixin, DeleteView):
    model = Software
    success_url = reverse_lazy('softwares')

