import argparse
import netCDF4 as nc 
import numpy as np
import os
import hashlib
import glob 
from datetime import datetime 
from datetime import timedelta


def search_year(file_path, word):
    with open(file_path, 'r') as fp:
        # read all content of a file
        lines = fp.readlines()
        for line in lines:
          if line.find(word) != -1:
            return(line[25:29]) 
def search_alt(file_path, word):
    with open(file_path, 'r') as fp:
        # read all content of a file
        lines = fp.readlines()
        for line in lines:
          if line.find(word) != -1:
            return(line[25:27])




years = [2019]
months = [6,7]
#days = [[0]*16]*2
days = [[24,25,26,27,28,29,30],[1,2,3,4,5,6,7,8,9,10,11]]
print('days[0,1] = ', days[1][0])
#days = day_list #[int(iday) for iday in day_list]
hours = [0,6,12,18]

xdim = 96 
ydim = 96
zdim = 127


# StaticB date

year_staticb = 2016
month_staticb = 6
day_staticb = 30
hour_staticb = 0
yyyymmdd_staticb = 20160630

output_path = '/scratch1/NCEPDEV/da/Andrew.Tangborn/JEDI/staticb_files/lagged/'

#ncyc=(len(day_list))*len(hour_list)
ncyc=(len(days[0][:])+len(days[1][:]))*len(hours)
so4_diff = np.empty((1,127,96,96,6,ncyc))
so4_diff_mean = np.empty((1,127,96,96,6))
so4_diff_rms = np.empty((1,127,96,96,6))
so4_diff_std = np.empty((1,127,96,96,6))
bc1_diff = np.empty((1,127,96,96,6,ncyc))
bc1_diff_mean = np.empty((1,127,96,96,6))
bc1_diff_rms = np.empty((1,127,96,96,6))
bc1_diff_std = np.empty((1,127,96,96,6))
bc2_diff = np.empty((1,127,96,96,6,ncyc))
bc2_diff_mean = np.empty((1,127,96,96,6))
bc2_diff_rms = np.empty((1,127,96,96,6))
bc2_diff_std = np.empty((1,127,96,96,6))
oc1_diff = np.empty((1,127,96,96,6,ncyc))
oc1_diff_mean = np.empty((1,127,96,96,6))
oc1_diff_rms = np.empty((1,127,96,96,6))
oc1_diff_std = np.empty((1,127,96,96,6))
oc2_diff = np.empty((1,127,96,96,6,ncyc))
oc2_diff_mean = np.empty((1,127,96,96,6))
oc2_diff_rms = np.empty((1,127,96,96,6))
oc2_diff_std = np.empty((1,127,96,96,6))
seas1_diff = np.empty((1,127,96,96,6,ncyc))
seas1_diff_mean = np.empty((1,127,96,96,6))
seas1_diff_rms = np.empty((1,127,96,96,6))
seas1_diff_std = np.empty((1,127,96,96,6))
seas2_diff = np.empty((1,127,96,96,6,ncyc))
seas2_diff_mean = np.empty((1,127,96,96,6))
seas2_diff_rms = np.empty((1,127,96,96,6))
seas2_diff_std = np.empty((1,127,96,96,6))
seas3_diff = np.empty((1,127,96,96,6,ncyc))
seas3_diff_mean = np.empty((1,127,96,96,6))
seas3_diff_rms = np.empty((1,127,96,96,6))
seas3_diff_std = np.empty((1,127,96,96,6))
seas4_diff = np.empty((1,127,96,96,6,ncyc))
seas4_diff_mean = np.empty((1,127,96,96,6))
seas4_diff_rms = np.empty((1,127,96,96,6))
seas4_diff_std = np.empty((1,127,96,96,6))
dust1_diff = np.empty((1,127,96,96,6,ncyc))
dust1_diff_mean = np.empty((1,127,96,96,6))
dust1_diff_rms = np.empty((1,127,96,96,6))
dust1_diff_std = np.empty((1,127,96,96,6))
dust2_diff = np.empty((1,127,96,96,6,ncyc))
dust2_diff_mean = np.empty((1,127,96,96,6))
dust2_diff_rms = np.empty((1,127,96,96,6))
dust2_diff_std = np.empty((1,127,96,96,6))
dust3_diff = np.empty((1,127,96,96,6,ncyc))
dust3_diff_mean = np.empty((1,127,96,96,6))
dust3_diff_rms = np.empty((1,127,96,96,6))
dust3_diff_std = np.empty((1,127,96,96,6))
dust4_diff = np.empty((1,127,96,96,6,ncyc))
dust4_diff_mean = np.empty((1,127,96,96,6))
dust4_diff_rms = np.empty((1,127,96,96,6))
dust4_diff_std = np.empty((1,127,96,96,6))
dust5_diff = np.empty((1,127,96,96,6,ncyc))
dust5_diff_mean = np.empty((1,127,96,96,6))
dust5_diff_rms = np.empty((1,127,96,96,6))
dust5_diff_std = np.empty((1,127,96,96,6))




exp_dir = '/scratch1/NCEPDEV/stmp2/Andrew.Tangborn/lagged_forecasts'


files = glob.glob(exp_dir+'/fcst.*/model_configure') 
year =  2019 
idat=0
for month in months:
  print('month=',month)
  month_index = months.index(month)
  print('month_index = ', month_index)
  for day_list in days[month_index][:]:
    print('day_list = ', day_list)
    for hour in hours:

      print('type(day_list) = ',type(day_list))
      day = int(day_list)
      print('type(year) = ', type(year))
      print('type(month) = ', type(month))
      print('type(day) = ', type(day))
      
      d =datetime(year,month,day) 
      d24 = d + timedelta(days=1)
      d48 = d + timedelta(days=2)
      s = d.strftime('%Y%m%d')
      s24 = d24.strftime('%Y%m%d')
      s48 = d48.strftime('%Y%m%d')
      print('string = ', s)
      yyyymmddhh = s+str(hour).zfill(2)
      yyyymmddhh_24 = s24+str(hour).zfill(2)
      yyyymmddhh24 = s24+'.'+str(hour).zfill(2)+'0000'
      yyyymmddhh48 = s48+'.'+str(hour).zfill(2)+'0000' 
      print('yyyymmddhh=',yyyymmddhh)
      print('yyyymmddhh+24 = ',yyyymmddhh24)
      print('yyyymmddhh+48 = ',yyyymmddhh48)
      print(exp_dir+'/fcst.'+yyyymmddhh+'/RESTART/'+yyyymmddhh48+'.fv_tracer.res.tile')
      print(exp_dir+'/fcst.'+yyyymmddhh_24+'/RESTART/'+yyyymmddhh48+'.fv_tracer.res.tile')
      files_48 = glob.glob(exp_dir+'/fcst.'+yyyymmddhh+'/RESTART/'+yyyymmddhh48+'.fv_tracer.res.tile*')
      files_24 = glob.glob(exp_dir+'/fcst.'+yyyymmddhh_24+'/RESTART/'+yyyymmddhh48+'.fv_tracer.res.tile*')
      itile = 0 
      while itile <=5 :
        filename24 = exp_dir+'/fcst.'+yyyymmddhh+'/RESTART/'+yyyymmddhh48+'.fv_tracer.res.tile'+str(itile+1)+'.nc' 
        print('filename24 = ', filename24)
        vars24 = nc.Dataset(filename24)
        so4_24 = vars24.variables['so4'][:,:,:]
        bc1_24 = vars24.variables['bc1'][:,:,:]
        bc2_24 = vars24.variables['bc2'][:,:,:]
        oc1_24 = vars24.variables['oc1'][:,:,:]
        oc2_24 = vars24.variables['oc2'][:,:,:]
        seas1_24 = vars24.variables['seas1'][:,:,:]
        seas2_24 = vars24.variables['seas2'][:,:,:]
        seas3_24 = vars24.variables['seas3'][:,:,:]
        seas4_24 = vars24.variables['seas4'][:,:,:]
        dust1_24 = vars24.variables['dust1'][:,:,:]
        dust2_24 = vars24.variables['dust2'][:,:,:]
        dust3_24 = vars24.variables['dust3'][:,:,:]
        dust4_24 = vars24.variables['dust4'][:,:,:]
        dust5_24 = vars24.variables['dust5'][:,:,:]
        filename48 = exp_dir+'/fcst.'+yyyymmddhh_24+'/RESTART/'+yyyymmddhh48+'.fv_tracer.res.tile'+str(itile+1)+'.nc' 
        print('filename48 = ', filename48)
        vars48 = nc.Dataset(filename48)
        so4_48 = vars48.variables['so4'][:,:,:] 
        bc1_48 = vars48.variables['bc1'][:,:,:]
        bc2_48 = vars48.variables['bc2'][:,:,:]
        oc1_48 = vars48.variables['oc1'][:,:,:]
        oc2_48 = vars48.variables['oc2'][:,:,:]
        seas1_48 = vars48.variables['seas1'][:,:,:]
        seas2_48 = vars48.variables['seas2'][:,:,:]
        seas3_48 = vars48.variables['seas3'][:,:,:]
        seas4_48 = vars48.variables['seas4'][:,:,:]
        dust1_48 = vars48.variables['dust1'][:,:,:]
        dust2_48 = vars48.variables['dust2'][:,:,:]
        dust3_48 = vars48.variables['dust3'][:,:,:]
        dust4_48 = vars48.variables['dust4'][:,:,:]
        dust5_48 = vars48.variables['dust5'][:,:,:]
        print('idat = ', idat)
        print('itile = ', itile)
        so4_diff[:,:,:,:,itile,idat] = so4_48 - so4_24
        bc1_diff[:,:,:,:,itile,idat] = bc1_48 - bc1_24 
        bc2_diff[:,:,:,:,itile,idat] = bc2_48 - bc2_24 
        oc1_diff[:,:,:,:,itile,idat] = oc1_48 - oc1_24 
        oc2_diff[:,:,:,:,itile,idat] = oc2_48 - oc2_24 
        seas1_diff[:,:,:,:,itile,idat] = seas1_48 - seas1_24
        seas2_diff[:,:,:,:,itile,idat] = seas2_48 - seas2_24
        seas3_diff[:,:,:,:,itile,idat] = seas3_48 - seas3_24
        seas4_diff[:,:,:,:,itile,idat] = seas4_48 - seas4_24
        dust1_diff[:,:,:,:,itile,idat] = dust1_48 - dust1_24
        dust2_diff[:,:,:,:,itile,idat] = dust2_48 - dust2_24
        dust3_diff[:,:,:,:,itile,idat] = dust3_48 - dust3_24
        dust4_diff[:,:,:,:,itile,idat] = dust4_48 - dust4_24
        dust5_diff[:,:,:,:,itile,idat] = dust5_48 - dust5_24
        itile = itile+1 
      idat = idat+1 
      
print('so4_48.shape=',so4_48.shape)
print('so4_diff.shape=',so4_diff.shape)
so4_diff_std[:,:,:,:,:] = np.std(so4_diff, axis = 5) 
print('so4_diff_std.max = ', np.nanmax(so4_diff_std))
bc1_diff_std[:,:,:,:,:] = np.std(bc1_diff, axis = 5) 
print('max bc1_diff_std = ',np.nanmax(bc1_diff_std))
bc2_diff_std[:,:,:,:,:] = np.std(bc2_diff, axis = 5) 
oc1_diff_std[:,:,:,:,:] = np.std(oc1_diff, axis = 5)
oc2_diff_std[:,:,:,:,:] = np.std(oc2_diff, axis = 5)
seas1_diff_std[:,:,:,:,:] = np.std(seas1_diff, axis = 5)
seas2_diff_std[:,:,:,:,:] = np.std(seas2_diff, axis = 5)
seas3_diff_std[:,:,:,:,:] = np.std(seas3_diff, axis = 5)
seas4_diff_std[:,:,:,:,:] = np.std(seas4_diff, axis = 5)
dust1_diff_std[:,:,:,:,:] = np.std(dust1_diff, axis = 5)
dust2_diff_std[:,:,:,:,:] = np.std(dust2_diff, axis = 5)
dust3_diff_std[:,:,:,:,:] = np.std(dust3_diff, axis = 5)
dust4_diff_std[:,:,:,:,:] = np.std(dust4_diff, axis = 5)
dust5_diff_std[:,:,:,:,:] = np.std(dust5_diff, axis = 5)


print(so4_diff_mean.shape)
print(so4_diff_rms.shape)
print(so4_diff_mean.shape)
  

# Write out standard deviations to netcdf files


itile = 0 
ntiles = 5 

while itile <= ntiles:


  str_stddev_output = str(yyyymmdd_staticb)+'.'+str(hour_staticb).zfill(2)+'0000.stddev.fv_tracer.res.tile'+str(itile+1)+'.nc'
  file_out = output_path+str_stddev_output
  ncfile_out = nc.Dataset(file_out, mode='w', format='NETCDF4')

  xaxis_1 = ncfile_out.createDimension("xaxis_1", xdim)
  xaxis_1 = ncfile_out.createVariable("xaxis_1", float, ('xaxis_1'))
  xaxis_1.long_name = 'xaxis_1'
  xaxis_1.units = 'none'
  xaxis_1.cartesian_axis = 'X'
  yaxis_1 = ncfile_out.createDimension("yaxis_1", ydim)
  yaxis_1 = ncfile_out.createVariable("yaxis_1", float, ('yaxis_1'))
  yaxis_1.long_name = 'yaxis_1'
  yaxis_1.units = 'none'
  yaxis_1.cartesian_axis = 'Y'
  zaxis_1 = ncfile_out.createDimension("zaxis_1", zdim)
  zaxis_1 = ncfile_out.createVariable("zaxis_1", float, ('zaxis_1'))
  zaxis_1.long_name = 'zaxis_1'
  zaxis_1.units = 'none'
  zaxis_1.cartesian_axis = 'Z'
  Time = ncfile_out.createDimension("Time",None )
  Time = ncfile_out.createVariable("Time", float, ('Time'))
  Time.long_name = 'Time'
  Time.units = 'time level'
  Time.cartesian_axis = 'T'

  so4=ncfile_out.createVariable('so4', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
  so4.long_name = 'mass_fraction_of_sulfate_in_air'
  so4.units = 'ugkg-1'
  so4.checksum = hashlib.md5("so4".encode('utf-8')).hexdigest()[:16]
  bc1=ncfile_out.createVariable('bc1', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
  bc1.long_name = 'mass_fraction_of_hydrophobic_black_carbon_in_air'
  bc1.units = 'ugkg-1'
  bc1.checksum = hashlib.md5("bc1".encode('utf-8')).hexdigest()[:16]
  bc2=ncfile_out.createVariable('bc2', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
  bc2.long_name = 'mass_fraction_of_hydrophilic_black_carbon_in_air'
  bc2.units = 'ugkg-1'
  bc2.checksum = hashlib.md5("bc2".encode('utf-8')).hexdigest()[:16]
  oc1=ncfile_out.createVariable('oc1', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
  oc1.long_name = 'mass_fraction_of_hydrophobic_organic_carbon_in_air'
  oc1.units = 'ugkg-1'
  oc1.checksum = hashlib.md5("oc1".encode('utf-8')).hexdigest()[:16]
  oc2=ncfile_out.createVariable('oc2', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
  oc2.long_name = 'mass_fraction_of_hydrophilic_organic_carbon_in_air'
  oc2.units = 'ugkg-1'
  oc2.checksum = hashlib.md5("oc2".encode('utf-8')).hexdigest()[:16]
  dust1=ncfile_out.createVariable('dust1', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
  dust1.long_name = 'mass_fraction_of_dust001_in_air'
  dust1.units = 'ugkg-1'
  dust1.checksum = hashlib.md5("dust1".encode('utf-8')).hexdigest()[:16]
  dust2=ncfile_out.createVariable('dust2', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
  dust2.long_name = 'mass_fraction_of_dust002_in_air'
  dust2.units = 'ugkg-1'
  dust2.checksum = hashlib.md5("dust2".encode('utf-8')).hexdigest()[:16]
  dust3=ncfile_out.createVariable('dust3', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
  dust3.long_name = 'mass_fraction_of_dust003_in_air'
  dust3.units = 'ugkg-1'
  dust3.checksum = hashlib.md5("dust3".encode('utf-8')).hexdigest()[:16]
  dust4=ncfile_out.createVariable('dust4', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
  dust4.long_name = 'mass_fraction_of_dust004_in_air'
  dust4.units = 'ugkg-1'
  dust4.checksum = hashlib.md5("dust4".encode('utf-8')).hexdigest()[:16]
  dust5=ncfile_out.createVariable('dust5', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
  dust5.long_name = 'mass_fraction_of_dust005_in_air'
  dust5.units = 'ugkg-1'
  dust5.checksum = hashlib.md5("dust5".encode('utf-8')).hexdigest()[:16]
  seas1=ncfile_out.createVariable('seas1', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
  seas1.long_name = 'mass_fraction_of_sea_salt001_in_air'
  seas1.units = 'ugkg-1'
  seas1.checksum = hashlib.md5("seas1".encode('utf-8')).hexdigest()[:16]
  seas2=ncfile_out.createVariable('seas2', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
  seas2.long_name = 'mass_fraction_of_sea_salt002_in_air'
  seas2.units = 'ugkg-1'
  seas2.checksum = hashlib.md5("seas2".encode('utf-8')).hexdigest()[:16]
  seas3=ncfile_out.createVariable('seas3', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
  seas3.long_name = 'mass_fraction_of_sea_salt003_in_air'
  seas3.units = 'ugkg-1'
  seas3.checksum = hashlib.md5("seas3".encode('utf-8')).hexdigest()[:16]
  seas4=ncfile_out.createVariable('seas4', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
  seas4.long_name = 'mass_fraction_of_sea_salt004_in_air'
  seas4.units = 'ugkg-1'
  seas4.checksum = hashlib.md5("seas4".encode('utf-8')).hexdigest()[:16]

  xaxis_1a = []
  yaxis_1a = []
  zaxis_1a = []
  for k in range(1,xdim+1):
    xaxis_1a += [k]
    yaxis_1a += [k]
  for k in range(1,zdim+1):
    zaxis_1a += [k]
  xaxis_1[:] = xaxis_1a[:]
  yaxis_1[:] = yaxis_1a[:]
  zaxis_1[:] = zaxis_1a[:]

  Time_a = []
  Time_a = [1]
  Time[:] = Time_a[:]

  print('so4.shape = ', so4.shape)
  print('so4_diff_std.shape = ', so4_diff_std.shape)
 
  print('so4_diff_std[:,:,:,itile].shape =', so4_diff_std[:,:,:,:,itile].shape)
  so4[:] = so4_diff_std[:,:,:,:,itile] 
  bc1[:] = bc1_diff_std[:,:,:,:,itile]
  bc2[:] = bc2_diff_std[:,:,:,:,itile]
  oc1[:] = oc1_diff_std[:,:,:,:,itile]
  oc2[:] = oc2_diff_std[:,:,:,:,itile]
  seas1[:] = seas1_diff_std[:,:,:,:,itile]
  seas2[:] = seas2_diff_std[:,:,:,:,itile]
  seas3[:] = seas3_diff_std[:,:,:,:,itile]
  seas4[:] = seas4_diff_std[:,:,:,:,itile]
  dust1[:] = dust1_diff_std[:,:,:,:,itile]
  dust2[:] = dust2_diff_std[:,:,:,:,itile]
  dust3[:] = dust3_diff_std[:,:,:,:,itile]
  dust4[:] = dust4_diff_std[:,:,:,:,itile]
  dust5[:] = dust5_diff_std[:,:,:,:,itile]

  ncfile_out.close
  itile = itile+1 





