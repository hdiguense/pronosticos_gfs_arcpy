#Descarga de datos
$fecha = (get-date).tostring("yyyyMMdd")
$url = "ftp://ftp.cpc.ncep.noaa.gov/GIS/gfs_0.25/gfs_precip_shp_tif_" + $fecha + ".zip"
$output = "D:\SIG\pronosticos\gfs.zip"
Invoke-WebRequest -Uri $url -OutFile $output
#Unzip
Expand-Archive D:\SIG\pronosticos\gfs.zip -DestinationPath D:\SIG\pronosticos\
