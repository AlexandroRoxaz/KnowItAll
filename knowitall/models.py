from django.db import models
from django.urls import reverse

class Building(models.Model):
#Fields

	Building_name=models.TextField(help_text="Enter text")
	Building_code=models.TextField(help_text="Enter text")

#Metadata
	class Meta:
		ordering = ['Building_name']

#Methods
	def get_absolute_url (self):
		return reverse('building-detail', args=[str(self.id)])
	def __str__(self):
		return self.Building_name

class Block(models.Model):
#Fields
	Block_name=models.TextField(help_text="Enter text")
	Block_number=models.TextField(help_text="Enter text")

#Metadata
	class Meta:
		ordering= ['Block_name']
#Methods
	def get_absolute_url (self):
		return reverse('block-detail', args=[str(self.id)])
	def __str__(self):
		return self.Block_name

class Project(models.Model):

	Project_name=models.TextField(help_text="Enter text")
	Project_def=models.TextField(help_text="Enter text")
#Metadata
	class Meta:
		ordering= ['Project_name']
#Methods
	def get_absolute_url (self):
		return reverse('project-detail', args=[str(self.id)])
	def __str__(self):
		return self.Project_name

class Subsystem(models.Model):

	Subsystem_name=models.TextField(help_text="Enter text")
	Subsystem_def=models.TextField(help_text="Enter text")
	Subsystem_project=models.ForeignKey('Project', on_delete=models.SET_NULL, null=True)
	Subsystem_block=models.ForeignKey('Block', on_delete=models.SET_NULL, null=True)
	class Meta: 
		ordering= ['Subsystem_name']
	def get_absoulte_url (self):
		return reverse('subsystem-detail', args=[str(self.id)])
	def __str__(self):
		return self.Subsystem_name

class Function(models.Model):

	Function_name=models.TextField(help_text="Enter text")
	Function_def=models.TextField(help_text="Enter text")
	class Meta:
		ordering= ['Function_name']
	def get_absolute_url (self):
		return reverse('function-detail', args=[str(self.id)])
	def __str__(self):
		return self.Function_name

class Location(models.Model):

	Location_name=models.TextField(help_text="Enter text")
	Location_code=models.TextField(help_text="Enter text")
	Location_building=models.ForeignKey('Building', on_delete=models.SET_NULL, null=True)
	class Meta:
		ordering= ['Location_name','Location_code']
	def get_absolute_url (self):
		return reverse('location-detail', args=[str(self.id)])
	def __str__(self):
		return self.Location_name

class Rack(models.Model):

	Rack_name=models.TextField(help_text="Enter text")
	Rack_KKS=models.TextField(help_text="Enter text")
	Rack_location=models.ForeignKey('Location', on_delete=models.SET_NULL, null=True) 
	Rack_TYPE=models.ForeignKey('Rack_TYPE', on_delete=models.SET_NULL, null=True)
	Rack_Subsystem=models.ForeignKey('Subsystem', on_delete=models.SET_NULL, null=True)
	class Meta:
		ordering= ['Rack_name','Rack_KKS']
	def get_absolute_url (self):
		return reverse('rack-detail', args=[str(self.id)])
	def __str__(self):
		return self.Rack_name

class Rack_TYPE(models.Model):
	Rack_TYPE_name=models.TextField(help_text="Enter text")
	Rack_TYPE_def=models.TextField(help_text="Enter text")
	
	class Meta:
		ordering= ['Rack_TYPE_name']
	def get_absolute_url (self):
		return reverse('racktype-detail', args=[str(self.id)])
	def __str__(self):
		return self.Rack_TYPE_name

class Interface(models.Model):
	Interface_name=models.TextField(help_text="Enter text")
	Interface_def=models.TextField(help_text="Enter text")

	class Meta:
		ordering= ['Interface_name','Interface_def']
	def get_absolute_url (self):
		return reverse('interface-detail', args=[str(self.id)])
	def __str__(self):
		return self.Interface_name

class PTS(models.Model):
	PTS_name=models.TextField(help_text="Enter text")
	PTS_code=models.TextField(help_text="Enter text")
	PTS_type=models.ForeignKey('PTS_TYPE', on_delete=models.SET_NULL, null=True)
	PTS_interface=models.ForeignKey('Interface', on_delete=models.SET_NULL, null=True)
	class Meta:
		ordering= ['PTS_name','PTS_code','PTS_type']
	def get_absolute_url (self):
		return reverse('pts-detail', args=[str(self.id)])
	def __str__(self):
		return self.PTS_name

class PTS_TYPE(models.Model):
	PTS_TYPE_name=models.TextField(help_text="Enter text")
	PTS_TYPE_def=models.TextField(help_text="Enter text")
	class Meta:
		ordering= ['PTS_TYPE_name','PTS_TYPE_def']
	def get_absolute_url (self):
		return reverse('ptstype-detail', args=[str(self.id)])
	def __str__(self):
		return self.PTS_TYPE_name

class Software(models.Model):
	Software_name=models.TextField(help_text="Enter text")
	Software_version=models.TextField(help_text="Enter text")
	Software_type=models.ForeignKey('Software_TYPE', on_delete=models.SET_NULL, null=True)

	class Meta:
		ordering= ['Software_name']
	def get_absolute_url (self):
		return reverse('software-detail', args=[str(self.id)])
	def __str__(self):
		return self.Software_name
	
class Software_TYPE(models.Model):
	Software_TYPE_name=models.TextField(help_text="Enter text")
	Software_TYPE_def=models.TextField(help_text="Enter text")

	class Meta:
		ordering=['Software_TYPE_name']
	def get_absolute_url (self):
		return reverse('softwaretype-detail', args=[str(self.id)])
	def __str__(self):
		return self.Software_TYPE_name
		
class PTS_SF(models.Model):
	PTS_id = models.ForeignKey('PTS', on_delete=models.SET_NULL, null=True)
	SF_id = models.ForeignKey('Software', on_delete=models.SET_NULL, null=True)

class PTS_INT(models.Model):
	PTS_id = models.ForeignKey('PTS', on_delete=models.SET_NULL, null=True)
	INT_id = models.ForeignKey('Interface', on_delete=models.SET_NULL, null=True)
	
class PTS_RACK(models.Model):
	PTS_id = models.ForeignKey('PTS', on_delete=models.SET_NULL, null=True)
	RACK_id = models.ForeignKey('Rack', on_delete=models.SET_NULL, null=True)
	
class PTS_FUNC(models.Model):
	PTS_id = models.ForeignKey('PTS', on_delete=models.SET_NULL, null=True)
	FUNC_id = models.ForeignKey('Function', on_delete=models.SET_NULL, null=True)
	
class SUBS_FUNC(models.Model):
	SUBS_id = models.ForeignKey('Subsystem', on_delete=models.SET_NULL, null=True)
	FUNC_id = models.ForeignKey('Function', on_delete=models.SET_NULL, null=True)

