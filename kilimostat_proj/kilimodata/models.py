from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 

length = 256
# Ignore this table was used for test
class Thematic(models.Model):
  themename = models.CharField(max_length=255)
  description = models.CharField(max_length=255)

# Ignore this table was used for test
class KilimoDomains(models.Model):
  sector = models.CharField(max_length=255)
  domain = models.CharField(max_length=255)
  subdomain = models.CharField(max_length=255)
  county = models.CharField(max_length=255)
  subcounty = models.CharField(max_length=255)
  ward = models.CharField(max_length=255)
  element = models.CharField(max_length=255)
  year = models.CharField(max_length=255)
  items = models.CharField(max_length=255)
  value = models.CharField(max_length=255)
  
  def __str__(self):
    return self.sector

# Use these table was used for test
class Institution(models.Model):
  id = models.AutoField(primary_key=True)   
  name = models.CharField(max_length=256, null=True)   
  date_created = models.DateTimeField(auto_now_add=True)
  def __str__(self):
        return str(self.name)


class DataEntryOfficer(models.Model): 
  id = models.AutoField(primary_key=True)   
  nationalid = models.CharField(max_length=256, null=True)
  firstname = models.CharField(max_length=256, null=True)
  lastname = models.CharField(max_length=256, null=True)     
  telephone = models.IntegerField(null=True)
  email = models.EmailField(max_length=256, null=True)
  designation = models.CharField(max_length=256, null=True)
  institution = models.ForeignKey(
    Institution, 
            on_delete=models.PROTECT, 
            null=True, 
            blank=True
    )
  date_created = models.DateTimeField(auto_now_add=True)
  def __str__(self):
        return str(self.nationalid)


class Sector(models.Model):    
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=256, null=True) 
  def __str__(self):
        return str(self.name)

class Domain(models.Model):    
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=256, null=True) 
  def __str__(self):
        return str(self.name)


class Subdomain(models.Model):    
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=256, null=True) 
  domain = models.ForeignKey(
    Domain, 
    on_delete=models.PROTECT, 
    null=True,
    blank=True
    )
  def __str__(self):
        return str(self.name)


class County(models.Model):    
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=256, null=True) 
  code = models.CharField(max_length=3, null=True) 
  def __str__(self):
        return str(self.name)
      

class SubCounty(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    county_id = models.ForeignKey('County', on_delete=models.CASCADE)
    name = models.CharField(max_length=length, blank=True, null=True,)
    lat = models.CharField(max_length=length, blank=True, null=True,)
    lng = models.CharField(max_length=length, blank=True, null=True,)
    category = models.CharField(max_length=length, blank=True, null=True,)
    code = models.CharField(max_length=length, blank=True, null=True,)
    loccode = models.CharField(max_length=length, blank=True, null=True,)

    def __str__(self):
        return '%s' % self.name


class Ward(models.Model):
    county_id = models.ForeignKey('County', on_delete=models.CASCADE)
    subcounty_id = models.ForeignKey('SubCounty', on_delete=models.CASCADE)
    name = models.CharField(max_length=length, blank=True, null=True,)
    lat = models.CharField(max_length=length, blank=True, null=True,)
    lng = models.CharField(max_length=length, blank=True, null=True,)
    category = models.CharField(max_length=length, blank=True, null=True,)
    code = models.CharField(max_length=length, blank=True, null=True,)
    loccode = models.CharField(max_length=length, blank=True, null=True,)

    def __str__(self):
        return '%s' % self.name

class Elements(models.Model):    
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=256, null=True) 
  def __str__(self):
        return str(self.name)

class ItemCategory(models.Model):    
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=256, null=True) 
  def __str__(self):
        return str(self.name)

class ItemSpecify(models.Model):    
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=256, null=True) 
  itemcategory = models.ForeignKey(
    ItemCategory, 
    on_delete=models.PROTECT, 
    null=False
    )
  def __str__(self):
        return str(self.name)

class Unit(models.Model):    
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=256, null=True) 
  def __str__(self):
        return str(self.name)


class KilimoData(models.Model):
  id = models.AutoField(primary_key=True)
  sector = models.ForeignKey(
    Sector, 
    on_delete=models.PROTECT, 
    null=False
    )

  subdomain = models.ForeignKey(
    Subdomain, 
    on_delete=models.PROTECT,
    null=False
    )

  county = models.ForeignKey(
    County, 
    on_delete=models.PROTECT, 
    null=False
    )
  
  subcounty = models.ForeignKey(SubCounty, 
    on_delete=models.PROTECT, 
    null=True)   
  ward = models.ForeignKey(Ward, 
    on_delete=models.PROTECT, 
    null=True) 

  elements = models.ForeignKey(
    Elements, 
    on_delete=models.PROTECT, 
    null=True,
    blank=True
    )

  itemspecify = models.ForeignKey(
    ItemSpecify, 
    on_delete=models.PROTECT,  
    null=True,
    blank=True
    )

  refyear = models.PositiveIntegerField(default=2021, validators=[MinValueValidator(1900), MaxValueValidator(2090)])

  value = models.FloatField()
  unit = models.ForeignKey(
    Unit, 
    on_delete=models.PROTECT,  
    null=True,
    blank=True
    )
  
  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)
