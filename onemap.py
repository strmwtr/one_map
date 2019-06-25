import arcpy

def create_onemap_feature(out_dir, out_name): 

  fields = [
    ['BufferType','Text',12],
    ['BufferWidthFeet','Short','NA'],
    ['CommunityAdvisoryCommittee','Text',100],
    ['Condition','Text',20],
    ['ConditionDate','Date','NA'],
    ['Curbs','Text',3],
    ['DataSource','Text',5],
    ['Easement','Text',3],
    ['LastEditor','Text',50],
    ['LastEditedDate','Date','NA'],
    ['MagisterialDistrict','Text',20],
    ['Maintenance','Text',20],
    ['Name','Text',100],
    ['Notes','Text',500],
    ['OwnerName','Text',100],
    ['OwnershipType','Text',25],
    ['Planning Status','Text',25],
    ['PriorityRank2018','Short','NA'],
    ['PriorityRank2019','Short','NA'],
    ['RoadAADT','Short','NA'],
    ['RoadSpeedLimit','Short','NA'],
    ['RouteName','Text',100],
    ['RouteNumber','Text',8],
    ['Signage','Text',3],
    ['SourceDocument','Text',100],
    ['Status','Text',9],
    ['SurfaceMaterial','Text',20],
    ['SurfaceCondition','Text',10],
    ['FacilityType','Text',25],
    ['WidthFeet','Short','NA'],
    ['YearBuilt','Short','NA']
    ]

  arcpy.CreateFeatureclass_management(
    out_path = out_location, 
    out_name = out_name,
    geometry_type = 'POLYLINE', 
    spatial_reference = "PROJCS['NAD_1983_StatePlane_Virginia_South_FIPS_4502_Feet',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',11482916.66666666],PARAMETER['False_Northing',3280833.333333333],PARAMETER['Central_Meridian',-78.5],PARAMETER['Standard_Parallel_1',36.76666666666667],PARAMETER['Standard_Parallel_2',37.96666666666667],PARAMETER['Latitude_Of_Origin',36.33333333333334],UNIT['Foot_US',0.3048006096012192]];-111140600 -91532100 3048.00609601219;-100000 10000;-100000 10000;3.28083333333333E-03;0.001;0.001;IsHighPrecision", 
    )

  for x in fields:
    if x[2] != 'NA':
      arcpy.AddField_management(
        in_table = r'{0}\{1}'.format(out_location, out_name), 
        field_name = x[0], 
        field_type = x[1],
        field_length = x[2])
    else:
      arcpy.AddField_management(
        in_table = r'{0}\{1}'.format(out_location, out_name), 
        field_name = x[0], 
        field_type = x[1])

arcpy.Delete_management(r'{0}\{1}'.format(out_location, out_name))
out_location = r'C:\Users\brownr\Desktop\db\PoncyA\OneMap\OneMap.gdb'
out_name = 'OneMap'
create_onemap_feature(out_location, out_name)