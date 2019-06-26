'''
Author: Bob Brown - brownr@charlottesville.org
Created: Summer 2019
Purpose: Create database and data structure for Bicycle and Pedestrian One Map project.
Repo: https://github.com/strmwtr/one_map
Req: Python 2. If you have ArcMap on your machine, you can run this version. If you have 
ArcPro, run onemap_py3.py instead.
'''
import arcpy

def one_map_gdb(out_dir, gdb_name):
  '''Creates geodatabase to house data.'''  
  arcpy.CreateFileGDB_management(out_dir, gdb_name)

def one_map_domains(gdb_path, domain_list):
  '''Creates the domains for the fields. Domains were outlined by One Map steering committee '''
  for dom in domain_list:
    arcpy.CreateDomain_management(gdb_path, dom[0], field_type = "TEXT")

def one_map_feature(gdb_path, out_name, out_ft, fields): 
  '''Creates One Map polyline feature class'''
  arcpy.CreateFeatureclass_management(
    out_path = gdb_path, 
    out_name = out_name,
    geometry_type = 'POLYLINE', 
    spatial_reference = "PROJCS['NAD_1983_StatePlane_Virginia_South_FIPS_4502_Feet',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',11482916.66666666],PARAMETER['False_Northing',3280833.333333333],PARAMETER['Central_Meridian',-78.5],PARAMETER['Standard_Parallel_1',36.76666666666667],PARAMETER['Standard_Parallel_2',37.96666666666667],PARAMETER['Latitude_Of_Origin',36.33333333333334],UNIT['Foot_US',0.3048006096012192]];-111140600 -91532100 3048.00609601219;-100000 10000;-100000 10000;3.28083333333333E-03;0.001;0.001;IsHighPrecision", 
    )

  for field in fields:
    if field[2] != 'NA':
      arcpy.AddField_management(
        in_table = out_ft, 
        field_name = field[0], 
        field_type = field[1],
        field_length = field[2])
    else:
      arcpy.AddField_management(
        in_table = out_ft, 
        field_name = field[0], 
        field_type = field[1])

def assign_domains(out_ft, fields):
  '''Assigns domains to OneMap features'''
  for field in fields:
    if field[3] != 'NA':
      arcpy.AssignDomainToField_management(out_ft, field[0], field[3])


def calls(out_dir):
  gdb_name = r'OneMap.gdb'
  out_name = 'OneMap'
  gdb_path = r'{0}\{1}'.format(out_dir,gdb_name)
  out_ft = r'{0}\{1}'.format(gdb_path,out_name)

  fields = [
    ['BufferType','Text',12, 'BufferType'],
    ['BufferWidthFeet','Short','NA','NA'],
    ['CommunityAdvisoryCommittee','Text',100,'NA'],
    ['Condition','Text',20,'NA'],
    ['ConditionDate','Date','NA','NA'],
    ['Curbs','Text',3,'NA'],
    ['DataSource','Text',5, 'DataSource'],
    ['Easement','Text',3, 'YN'],
    ['LastEditor','Text',50,'NA'],
    ['LastEditedDate','Date','NA','NA'],
    ['MagisterialDistrict','Text',20,'MagisterialDistrict'],
    ['Maintenance','Text',20,'NA'],
    ['Name','Text',100,'NA'],
    ['Notes','Text',500,'NA'],
    ['OwnerName','Text',100,'NA'],
    ['OwnershipType','Text',25,'OwnershipType'],
    ['PlanningStatus','Text',25,'PlanningStatus'],
    ['PriorityRank2018','Short','NA','NA'],
    ['PriorityRank2019','Short','NA','NA'],
    ['RoadAADT','Short','NA','NA'],
    ['RoadSpeedLimit','Short','NA','NA'],
    ['RouteName','Text',100,'NA'],
    ['RouteNumber','Text',8,'NA'],
    ['Signage','Text',3,'YN'],
    ['SourceDocument','Text',100,'NA'],
    ['Status','Text',9,'Status'],
    ['SurfaceMaterial','Text',20,'NA'],
    ['SurfaceCondition','Text',10,'NA'],
    ['FacilityType','Text',25,'FacilityType'],
    ['WidthFeet','Short','NA','NA'],
    ['YearBuilt','Short','NA','NA']
    ]

  domain_list = [    
    ['BufferType','Text',['Barrier', 'Parking Lane', 'Delineators', 'None']],
    ['DataSource','Text',['County', 'City', 'TJPDC', 'UVA']],
    ['MagisterialDistrict','Text',['Rivanna', 'Scottsville', 'White Hall', 'Jack Jouett', 'Samuel Miller', 'Rio', 'City']],
    ['OwnershipType','Text',['Public', 'Private', 'Private with Easement']],
    ['PlanningStatus','Text',['Proposed', 'Prioritized', 'Planning', 'Design', 'Application Submitted', 'Funded', 'Under Construction', 'Complete']],
    ['Status','Text',['Exisiting', 'Future']],
    ['FacilityType','Text',['Sidewalk', 'Urban Sidewalk', 'Pedestrian Path', 'Shared Roadway', 'Bike Lane', 'Paved Shoulder', 'Shared Use Path', 'Urban Shared Use Path', 'Trail Class A', 'Trail Class B']],
    ['YN','TEXT',['YES', 'NO', 'NA']] #Easement, Curbs, Signage 
    ]
        
  arcpy.Delete_management(gdb_path)
  one_map_gdb(out_dir,out_name)
  one_map_domains(gdb_path, domain_list)
  one_map_feature(gdb_path, out_name, out_ft, fields)
  assign_domains(out_ft, fields)

calls(r'C:\Users\brownr\Desktop\db\PoncyA\OneMap')