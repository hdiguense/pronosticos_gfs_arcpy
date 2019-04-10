# -*- coding: UTF-8 -*-

#import system modules
import arcpy
from arcpy import env
import xml.dom.minidom as DOM 

#set env
project_folder = r'D:\SIG\pronosticos'
env.workspace = project_folder
arcpy.env.overwriteOutput = True

#date
date = datetime.datetime.today().strftime('%Y%m%d')

#default paths
gfs_today = project_folder + r'\gfs_precip_shp_tif_' + date
gfs_24h = gfs_today + r'\gfs_precip_gis_24_' + date + r'.shp'
gfs_48h = gfs_today + r'\gfs_precip_gis_48_' + date + r'.shp'
gfs_72h = gfs_today + r'\gfs_precip_gis_72_' + date + r'.shp'
gfs_96h = gfs_today + r'\gfs_precip_gis_96_' + date + r'.shp'
gfs_120h = gfs_today + r'\gfs_precip_gis_120_' + date + r'.shp'
gfs_144h = gfs_today + r'\gfs_precip_gis_144_' + date + r'.shp'
gfs_168h = gfs_today + r'\gfs_precip_gis_168_' + date + r'.shp'
gfs_7day = gfs_today + r'\gfs_precip_gis_7day_' + date + r'.shp'
costa_rica = project_folder + r'\pronosticos\default.gdb\costa_rica'
project_gdb = project_folder + r'\pronosticos\default.gdb'


#outputs
gfs_24h_cr = project_gdb + r'\gfs_24h_cr'
gfs_48h_cr = project_gdb + r'\gfs_48h_cr'
gfs_72h_cr = project_gdb + r'\gfs_72h_cr'
gfs_96h_cr = project_gdb + r'\gfs_96h_cr'
gfs_120h_cr = project_gdb + r'\gfs_120h_cr'
gfs_144h_cr = project_gdb + r'\gfs_144h_cr'
gfs_168h_cr = project_gdb + r'\gfs_168h_cr'
gfs_7day_cr = project_gdb + r'\gfs_7day_cr'

#import arcgis project aprx
aprx = arcpy.mp.ArcGISProject(project_folder + r'\pronosticos\pronosticos.aprx')

#clip 24 hours
arcpy.Clip_analysis(gfs_24h,costa_rica,gfs_24h_cr)
#create_time_fields
arcpy.AddField_management(gfs_24h_cr,'inicio', 'DATE')
arcpy.AddField_management(gfs_24h_cr,'final', 'DATE')
#Calculate start and end dates
arcpy.CalculateField_management(gfs_24h_cr, 'inicio','datetime.datetime.now().replace(hour=0, minute=0, second=0)')
arcpy.CalculateField_management(gfs_24h_cr, 'final','datetime.datetime.now().replace(hour=23, minute=59, second=59)')

#clip 48 hours
arcpy.Clip_analysis(gfs_48h,costa_rica,gfs_48h_cr)
#create_time_fields
arcpy.AddField_management(gfs_48h_cr,'inicio', 'DATE')
arcpy.AddField_management(gfs_48h_cr,'final', 'DATE')
#Calculate start and end dates
arcpy.CalculateField_management(gfs_48h_cr, 'inicio','datetime.datetime.now().replace(hour=0, minute=0, second=0) + datetime.timedelta(days=1)', 'PYTHON3')
arcpy.CalculateField_management(gfs_48h_cr, 'final','datetime.datetime.now().replace(hour=23, minute=59, second=59) + datetime.timedelta(days=1)', 'PYTHON3')

#clip 72 hours
arcpy.Clip_analysis(gfs_72h,costa_rica,gfs_72h_cr)
#create_time_fields
arcpy.AddField_management(gfs_72h_cr,'inicio', 'DATE')
arcpy.AddField_management(gfs_72h_cr,'final', 'DATE')
#Calculate start and end dates
arcpy.CalculateField_management(gfs_72h_cr, 'inicio','datetime.datetime.now().replace(hour=0, minute=0, second=0) + datetime.timedelta(days=2)', 'PYTHON3')
arcpy.CalculateField_management(gfs_72h_cr, 'final','datetime.datetime.now().replace(hour=23, minute=59, second=59) + datetime.timedelta(days=2)', 'PYTHON3')

#clip 96 hours
arcpy.Clip_analysis(gfs_96h,costa_rica,gfs_96h_cr)
#create_time_fields
arcpy.AddField_management(gfs_96h_cr,'inicio', 'DATE')
arcpy.AddField_management(gfs_96h_cr,'final', 'DATE')
#Calculate start and end dates
arcpy.CalculateField_management(gfs_96h_cr, 'inicio','datetime.datetime.now().replace(hour=0, minute=0, second=0) + datetime.timedelta(days=3)', 'PYTHON3')
arcpy.CalculateField_management(gfs_96h_cr, 'final','datetime.datetime.now().replace(hour=23, minute=59, second=59) + datetime.timedelta(days=3)', 'PYTHON3')

#clip 120 hours
arcpy.Clip_analysis(gfs_120h,costa_rica,gfs_120h_cr)
#create_time_fields
arcpy.AddField_management(gfs_120h_cr,'inicio', 'DATE')
arcpy.AddField_management(gfs_120h_cr,'final', 'DATE')
#Calculate start and end dates
arcpy.CalculateField_management(gfs_120h_cr, 'inicio','datetime.datetime.now().replace(hour=0, minute=0, second=0) + datetime.timedelta(days=4)', 'PYTHON3')
arcpy.CalculateField_management(gfs_120h_cr, 'final','datetime.datetime.now().replace(hour=23, minute=59, second=59) + datetime.timedelta(days=4)', 'PYTHON3')

#clip 144 hours
arcpy.Clip_analysis(gfs_144h,costa_rica,gfs_144h_cr)
#create_time_fields
arcpy.AddField_management(gfs_144h_cr,'inicio', 'DATE')
arcpy.AddField_management(gfs_144h_cr,'final', 'DATE')
#Calculate start and end dates
arcpy.CalculateField_management(gfs_144h_cr, 'inicio','datetime.datetime.now().replace(hour=0, minute=0, second=0) + datetime.timedelta(days=5)', 'PYTHON3')
arcpy.CalculateField_management(gfs_144h_cr, 'final','datetime.datetime.now().replace(hour=23, minute=59, second=59) + datetime.timedelta(days=5)', 'PYTHON3')

#clip 168 hours
arcpy.Clip_analysis(gfs_168h,costa_rica,gfs_168h_cr)
#create_time_fields
arcpy.AddField_management(gfs_168h_cr,'inicio', 'DATE')
arcpy.AddField_management(gfs_168h_cr,'final', 'DATE')
#Calculate start and end dates
arcpy.CalculateField_management(gfs_168h_cr, 'inicio','datetime.datetime.now().replace(hour=0, minute=0, second=0) + datetime.timedelta(days=6)', 'PYTHON3')
arcpy.CalculateField_management(gfs_168h_cr, 'final','datetime.datetime.now().replace(hour=23, minute=59, second=59) + datetime.timedelta(days=6)', 'PYTHON3')

#clip 7 days
arcpy.Clip_analysis(gfs_7day,costa_rica,gfs_7day_cr)
#create_time_fields
arcpy.AddField_management(gfs_7day_cr,'inicio', 'DATE')
arcpy.AddField_management(gfs_7day_cr,'final', 'DATE')
#Calculate start and end dates
arcpy.CalculateField_management(gfs_7day_cr, 'inicio','datetime.datetime.now().replace(hour=0, minute=0, second=0)', 'PYTHON3')
arcpy.CalculateField_management(gfs_7day_cr, 'final','datetime.datetime.now().replace(hour=23, minute=59, second=59) + datetime.timedelta(days=6)', 'PYTHON3')

#Merge of all cliped layers
arcpy.Merge_management([gfs_24h_cr, gfs_48h_cr, gfs_72h_cr, gfs_96h_cr, gfs_120h_cr, gfs_144h_cr, gfs_168h_cr], project_gdb + r'\precipitacion','Contour "Contour" true true false 4 Long 0 0,First,#,gfs_168h_cr,Contour,-1,-1,gfs_120h_cr,Contour,-1,-1,gfs_144h_cr,Contour,-1,-1,gfs_24h_cr,Contour,-1,-1,gfs_48h_cr,Contour,-1,-1,gfs_72h_cr,Contour,-1,-1,gfs_96h_cr,Contour,-1,-1;nVerts "nVerts" true true false 4 Long 0 0,First,#,gfs_168h_cr,nVerts,-1,-1,gfs_120h_cr,nVerts,-1,-1,gfs_144h_cr,nVerts,-1,-1,gfs_24h_cr,nVerts,-1,-1,gfs_48h_cr,nVerts,-1,-1,gfs_72h_cr,nVerts,-1,-1,gfs_96h_cr,nVerts,-1,-1;Title "Title" true true false 59 Text 0 0,First,#,gfs_168h_cr,Title,0,59,gfs_120h_cr,Title,0,59,gfs_144h_cr,Title,0,59,gfs_24h_cr,Title,0,58,gfs_48h_cr,Title,0,58,gfs_72h_cr,Title,0,58,gfs_96h_cr,Title,0,58;Unit "Unit" true true false 11 Text 0 0,First,#,gfs_168h_cr,Unit,0,11,gfs_120h_cr,Unit,0,11,gfs_144h_cr,Unit,0,11,gfs_24h_cr,Unit,0,11,gfs_48h_cr,Unit,0,11,gfs_72h_cr,Unit,0,11,gfs_96h_cr,Unit,0,11;Resolution "Resolution" true true false 18 Text 0 0,First,#,gfs_168h_cr,Resolution,0,18,gfs_120h_cr,Resolution,0,18,gfs_144h_cr,Resolution,0,18,gfs_24h_cr,Resolution,0,18,gfs_48h_cr,Resolution,0,18,gfs_72h_cr,Resolution,0,18,gfs_96h_cr,Resolution,0,18;Shape_Length "Shape_Length" false true true 8 Double 0 0,First,#,gfs_168h_cr,Shape_Length,-1,-1,gfs_120h_cr,Shape_Length,-1,-1,gfs_144h_cr,Shape_Length,-1,-1,gfs_24h_cr,Shape_Length,-1,-1,gfs_48h_cr,Shape_Length,-1,-1,gfs_72h_cr,Shape_Length,-1,-1,gfs_96h_cr,Shape_Length,-1,-1;Shape_Area "Shape_Area" false true true 8 Double 0 0,First,#,gfs_168h_cr,Shape_Area,-1,-1,gfs_120h_cr,Shape_Area,-1,-1,gfs_144h_cr,Shape_Area,-1,-1,gfs_24h_cr,Shape_Area,-1,-1,gfs_48h_cr,Shape_Area,-1,-1,gfs_72h_cr,Shape_Area,-1,-1,gfs_96h_cr,Shape_Area,-1,-1;inicio "inicio" true true false 8 Date 0 0,First,#,gfs_168h_cr,inicio,-1,-1,gfs_120h_cr,inicio,-1,-1,gfs_144h_cr,inicio,-1,-1,gfs_24h_cr,inicio,-1,-1,gfs_48h_cr,inicio,-1,-1,gfs_72h_cr,inicio,-1,-1,gfs_96h_cr,inicio,-1,-1;final "final" true true false 8 Date 0 0,First,#,gfs_168h_cr,final,-1,-1,gfs_120h_cr,final,-1,-1,gfs_144h_cr,final,-1,-1,gfs_24h_cr,final,-1,-1,gfs_48h_cr,final,-1,-1,gfs_72h_cr,final,-1,-1,gfs_96h_cr,final,-1,-1')

#save project
aprx.save()

#connect to arcgis portal
#arcpy.SignInToPortal_server("adminicafe","icafesig", "https://sig.icafe.cr/")

#Create sddraft
m =  aprx.listMaps('Map')[0]
arcpy.mp.CreateWebLayerSDDraft(m, project_folder + r'\pronosticos.sddraft','Pronosticos','MY_HOSTED_SERVICES','',True, 'Pronosticos','Pronosticos GFS','Pronosticos')

#set variables to overwrite service
inServiceDefinitionDraft = project_folder + r'\pronosticos.sddraft'
outServiceDefinition = project_folder + r'\pronosticos.sd'
newType = 'esriServiceDefinitionType_Replacement'

xml =  project_folder + r'\pronosticos.sddraft'
doc = DOM.parse(xml)
descriptions = doc.getElementsByTagName('Type')
for desc in descriptions:
    if desc.parentNode.tagName == 'SVCManifest':
        if desc.hasChildNodes():
             desc.firstChild.data = newType

f = open(xml, 'w')     
doc.writexml( f )     
f.close()

# Execute StageService
arcpy.StageService_server(inServiceDefinitionDraft, outServiceDefinition)

# Execute UploadServiceDefinition
arcpy.UploadServiceDefinition_server(outServiceDefinition, 'My Hosted Services')