# -*- coding: utf-8 -*-
#import neccessary modules
import netCDF4 as nc
import numpy as np
import datetime
from matplotlib.dates import date2num
import time

#TNN DJF
#determine lat and lon of medoids
med = nc.Dataset('/srv/ccrc/data06/z5147939/ncfiles/clust_3m/tnn_DJF_2016_K_7_sil_0.1.nc', mode='r')
med_lon = med.variables['medoid_lon'][:]
med_lat = med.variables['medoid_lat'][:]

#bring in tnn dataset 
ts = nc.Dataset('/srv/ccrc/data06/z5147939/ncfiles/era/tnn_ei_3m_DJF.nc', mode='r')
lons = ts.variables['lon'][:]
lats = ts.variables['lat'][:]
#time = ts.variables['time'][:]
#units = ts.variables['time'].units

#determine indices for lats and lons of medoids

def geo_idx(dd, dd_array):
   """
     search for nearest decimal degree in an array of decimal degrees and return the index.
     np.argmin returns the indices of minium value along an axis.
     so subtract dd from all values in dd_array, take absolute value and find index of minium.
    """
   geo_idx = (np.abs(dd_array - dd)).argmin()
   return geo_idx

lat_idx_n1 = geo_idx(med_lat[0], lats)
lon_idx_n1 = geo_idx(med_lon[0], lons)

lat_idx_n2 = geo_idx(med_lat[1], lats)
lon_idx_n2 = geo_idx(med_lon[1], lons)

lat_idx_n3 = geo_idx(med_lat[2], lats)
lon_idx_n3 = geo_idx(med_lon[2], lons)

lat_idx_n4 = geo_idx(med_lat[3], lats)
lon_idx_n4 = geo_idx(med_lon[3], lons)

lat_idx_n5 = geo_idx(med_lat[4], lats)
lon_idx_n5 = geo_idx(med_lon[4], lons)

lat_idx_n6 = geo_idx(med_lat[5], lats)
lon_idx_n6 = geo_idx(med_lon[5], lons)

lat_idx_n7 = geo_idx(med_lat[6], lats)
lon_idx_n7 = geo_idx(med_lon[6], lons)

#lat_idx_n8 = geo_idx(med_lat[7], lats)
#lon_idx_n8 = geo_idx(med_lon[7], lons)

#lat_idx_n9 = geo_idx(med_lat[8], lats)
#lon_idx_n9 = geo_idx(med_lon[8], lons)

#lat_idx_n10 = geo_idx(med_lat[9], lats)
#lon_idx_n10 = geo_idx(med_lon[9], lons)

#lat_idx_n11 = geo_idx(med_lat[10], lats)
#lon_idx_n11 = geo_idx(med_lon[10], lons)

#lat_idx_n12 = geo_idx(med_lat[11], lats)
#lon_idx_n12 = geo_idx(med_lon[11], lons)

#lat_idx_n13 = geo_idx(med_lat[12], lats)
#lon_idx_n13 = geo_idx(med_lon[12], lons)





#print 'The latitude and longitude indices for n1 are %d and %d' % (lat_idx_n1, lon_idx_n1)
#print 'The latitude and longitude indices for n2 are %d and %d' % (lat_idx_n2, lon_idx_n2)
#print 'The latitude and longitude indices for n3 are %d and %d' % (lat_idx_n3, lon_idx_n3)



#clusters
ts = nc.Dataset('/srv/ccrc/data06/z5147939/datasets/era/tnn_era_1979-2016_aus.nc', mode='r')
day_c1 = ts.variables['day'][:,lat_idx_n1,lon_idx_n1]
day_c4 = ts.variables['day'][:,lat_idx_n2, lon_idx_n2]
day_c2 = ts.variables['day'][:,lat_idx_n3,lon_idx_n3]
day_c6 = ts.variables['day'][:,lat_idx_n4,lon_idx_n4]
day_c7 = ts.variables['day'][:,lat_idx_n5,lon_idx_n5]
day_c5 = ts.variables['day'][:,lat_idx_n6,lon_idx_n6]
day_c3 = ts.variables['day'][:,lat_idx_n7,lon_idx_n7]
#day_c6 = ts.variables['day'][:,lat_idx_n8,lon_idx_n8]
#day_c1 = ts.variables['day'][:,lat_idx_n9,lon_idx_n9]
#day_c13 = ts.variables['day'][:,lat_idx_n10,lon_idx_n10]
#day_c9 = ts.variables['day'][:,lat_idx_n11,lon_idx_n11]
#day_c11 = ts.variables['day'][:,lat_idx_n12,lon_idx_n12]
#day_c10 = ts.variables['day'][:,lat_idx_n13,lon_idx_n13]



#mslp
ds_mslp = nc.Dataset('/srv/ccrc/data06/z5147939/datasets/era/psl_era_daymn_red.nc', mode='r')
mslp = ds_mslp.variables['psl'][:]
time = ds_mslp.variables['time'][:]
calendar = ds_mslp.variables['time'].calendar
units = ds_mslp.variables['time'].units
lon = ds_mslp.variables['lon'][:]
lat = ds_mslp.variables['lat'][:]


#change time from netcdf format to datetime
datevar = nc.num2date(time, units, calendar=calendar)
#print time, datevar
#define empty arrays for years, months, days
years = np.zeros(((len(datevar),)))
months = np.zeros(((len(datevar),)))
days = np.zeros(((len(datevar),)))
#loop to fill empty arrays with datetime to separate each time scale
for i in range(0,len(datevar)):
  years[i] = datevar[i].year
  months[i] = datevar[i].month
  days[i] = datevar[i].day

mslp_c1 = np.zeros(((12*(2017-1979)), len(lat), len(lon)), dtype='float32')
mslp_c2 = np.zeros(((12*(2017-1979)), len(lat), len(lon)), dtype='float32')
mslp_c3 = np.zeros(((12*(2017-1979)), len(lat), len(lon)), dtype='float32')
mslp_c4 = np.zeros(((12*(2017-1979)), len(lat), len(lon)), dtype='float32')
mslp_c5 = np.zeros(((12*(2017-1979)), len(lat), len(lon)), dtype='float32')
mslp_c6 = np.zeros(((12*(2017-1979)), len(lat), len(lon)), dtype='float32')
mslp_c7 = np.zeros(((12*(2017-1979)), len(lat), len(lon)), dtype='float32')
#mslp_c8 = np.zeros(((12*(2017-1979)), len(lat), len(lon)), dtype='float32')
#mslp_c9 = np.zeros(((12*(2017-1979)), len(lat), len(lon)), dtype='float32')
#mslp_c10 = np.zeros(((12*(2017-1979)), len(lat), len(lon)), dtype='float32')
#mslp_c11 = np.zeros(((12*(2017-1979)), len(lat), len(lon)), dtype='float32')
#mslp_c12 = np.zeros(((12*(2017-1979)), len(lat), len(lon)), dtype='float32')
#mslp_c13 = np.zeros(((12*(2017-1979)), len(lat), len(lon)), dtype='float32')

year_l = range(1979,2017) 
#year_l = range(1979,1981) 
month_l = range(1,13)

#loop through lats, lons, years and months
for i in range(0,len(lat)):
#for i in range(0,2):
  for j in range(0,len(lon)):
  #for j in range(0,2):
    t=0
    for y in range(0,len(year_l)):
      #indices for each year 
      i_year = np.squeeze(np.where(years == year_l[y]))
      for m in range(0,len(month_l)):
	#indices for each month
	i_month = np.squeeze(np.where(months[i_year] == month_l[m]))
	i_day_c1 = np.squeeze(np.where(days[i_year[i_month]] == day_c1[t]))
	i_day_c2 = np.squeeze(np.where(days[i_year[i_month]] == day_c2[t]))
	i_day_c3 = np.squeeze(np.where(days[i_year[i_month]] == day_c3[t]))
	i_day_c4 = np.squeeze(np.where(days[i_year[i_month]] == day_c4[t]))
	i_day_c5 = np.squeeze(np.where(days[i_year[i_month]] == day_c5[t]))
	i_day_c6 = np.squeeze(np.where(days[i_year[i_month]] == day_c6[t]))
	i_day_c7 = np.squeeze(np.where(days[i_year[i_month]] == day_c7[t]))
	#i_day_c8 = np.squeeze(np.where(days[i_year[i_month]] == day_c8[t]))
	#i_day_c9 = np.squeeze(np.where(days[i_year[i_month]] == day_c9[t]))
	#i_day_c10 = np.squeeze(np.where(days[i_year[i_month]] == day_c10[t]))
	#i_day_c11 = np.squeeze(np.where(days[i_year[i_month]] == day_c11[t]))
	#i_day_c12 = np.squeeze(np.where(days[i_year[i_month]] == day_c12[t]))
	#i_day_c13 = np.squeeze(np.where(days[i_year[i_month]] == day_c13[t]))
	#print mslp[i_year[i_month[i_day_c2]],i,j], day_c2[t], month_l[m], year_l[y] 
	mslp_c1[t,i,j]  = mslp[i_year[i_month[i_day_c1]],i,j]
	mslp_c2[t,i,j]  = mslp[i_year[i_month[i_day_c2]],i,j]
	mslp_c3[t,i,j]  = mslp[i_year[i_month[i_day_c3]],i,j]
	mslp_c4[t,i,j]  = mslp[i_year[i_month[i_day_c4]],i,j]
	mslp_c5[t,i,j]  = mslp[i_year[i_month[i_day_c5]],i,j]
	mslp_c6[t,i,j]  = mslp[i_year[i_month[i_day_c6]],i,j]
	mslp_c7[t,i,j]  = mslp[i_year[i_month[i_day_c7]],i,j]
	#mslp_c8[t,i,j]  = mslp[i_year[i_month[i_day_c8]],i,j]
	#mslp_c9[t,i,j]  = mslp[i_year[i_month[i_day_c9]],i,j]
	#mslp_c10[t,i,j]  = mslp[i_year[i_month[i_day_c10]],i,j]
	#mslp_c11[t,i,j]  = mslp[i_year[i_month[i_day_c11]],i,j]
	#mslp_c12[t,i,j]  = mslp[i_year[i_month[i_day_c12]],i,j]
	#mslp_c13[t,i,j]  = mslp[i_year[i_month[i_day_c13]],i,j]
	#print mslp_c1[t,i,j], mslp_c2[t,i,j], mslp_c3[t,i,j]
	t=t+1

#define time axis from 1979-2013 at the 15th of each month
startyear = 1979
startmonth = 1
endyear = 2016
endmonth = 12
time_dates = np.asarray([datetime.datetime(m/12, m%12+1, 15, 0, 0) for m in xrange(startyear*12+startmonth-1, endyear*12+endmonth)])
#print time_dates
#change to numbers
time_axis = nc.date2num(time_dates, units, calendar='standard')
#print time_axis


#write nc file 
f = nc.Dataset('/srv/ccrc/data06/z5147939/datasets/era/mslp_tnn_djf_7clust.nc','w')

#create dimensions
f.createDimension('lon', len(lon))
f.createDimension('lat', len(lat))
f.createDimension('time', None)

#create variables

#longitude
lons = f.createVariable('lon', 'f4', ('lon',))
lons.long_name='Longitude'
lons.units = 'degrees_east'

#latitude
lats = f.createVariable('lat', 'f4', ('lat',))  
lats.long_name = 'Latitude'
lats.units = 'degrees_north'


#time
times = f.createVariable('time', 'f4', ('time',))
times.long_name = 'time'
times.units = 'hours since 1900-1-1 00:00:00' 


#create 3D variables
#mslp_c1
mslp_c1_v = f.createVariable('mslp_c1', 'f4', ('time', 'lat', 'lon',))
mslp_c1_v.long_name='Low cloud cover occurring when medoid 1 is at tnn'
mslp_c1_v.units='Fraction'

#mslp_c2
mslp_c2_v = f.createVariable('mslp_c2', 'f4', ('time', 'lat', 'lon',))
mslp_c2_v.long_name='Low cloud cover occurring when medoid 2 is at tnn'
mslp_c2_v.units='Fraction'

#mslp_c3
mslp_c3_v = f.createVariable('mslp_c3', 'f4', ('time', 'lat', 'lon',))
mslp_c3_v.long_name='Low cloud cover occurring when medoid 2 is at tnn'
mslp_c3_v.units='Fraction'

#mslp_c4
mslp_c4_v = f.createVariable('mslp_c4', 'f4', ('time', 'lat', 'lon',))
mslp_c4_v.long_name='Low cloud cover occurring when medoid 4 is at tnn'
mslp_c4_v.units='Fraction'

#mslp_c5
mslp_c5_v = f.createVariable('mslp_c5', 'f4', ('time', 'lat', 'lon',))
mslp_c5_v.long_name='Low cloud cover occurring when medoid 5 is at tnn'
mslp_c5_v.units='Fraction'

#mslp_c6
mslp_c6_v = f.createVariable('mslp_c6', 'f4', ('time', 'lat', 'lon',))
mslp_c6_v.long_name='Low cloud cover occurring when medoid 6 is at tnn'
mslp_c6_v.units='Fraction'


#mslp_c7
mslp_c7_v = f.createVariable('mslp_c7', 'f4', ('time', 'lat', 'lon',))
mslp_c7_v.long_name='Low cloud cover occurring when medoid 7 is at tnn'
mslp_c7_v.units='Fraction'

##mslp_c8
#mslp_c8_v = f.createVariable('mslp_c8', 'f4', ('time', 'lat', 'lon',))
#mslp_c8_v.long_name='Low cloud cover occurring when medoid 8 is at tnn'
#mslp_c8_v.units='Fraction'

##mslp_c9
#mslp_c9_v = f.createVariable('mslp_c9', 'f4', ('time', 'lat', 'lon',))
#mslp_c9_v.long_name='Low cloud cover occurring when medoid 9 is at tnn'
#mslp_c9_v.units='Fraction'

##mslp_c10
#mslp_c10_v = f.createVariable('mslp_c10', 'f10', ('time', 'lat', 'lon',))
#mslp_c10_v.long_name='Low cloud cover occurring when medoid 10 is at tnn'
#mslp_c10_v.units='Fraction'

##mslp_c11
#mslp_c11_v = f.createVariable('mslp_c11', 'f4', ('time', 'lat', 'lon',))
#mslp_c11_v.long_name='Low cloud cover occurring when medoid 11 is at tnn'
#mslp_c11_v.units='Fraction'


##mslp_c12
#mslp_c12_v = f.createVariable('mslp_c12', 'f4', ('time', 'lat', 'lon',))
#mslp_c12_v.long_name='Low cloud cover occurring when medoid 12 is at tnn'
#mslp_c12_v.units='Fraction'

##mslp_c13
#mslp_c13_v = f.createVariable('mslp_c13', 'f4', ('time', 'lat', 'lon',))
#mslp_c13_v.long_name='Low cloud cover occurring when medoid 13 is at tnn'
#mslp_c13_v.units='Fraction'



#write data to variables
times[:] = time_axis
lons[:] = lon
lats[:] = lat
mslp_c1_v[:] = mslp_c1
mslp_c2_v[:] = mslp_c2
mslp_c3_v[:] = mslp_c3
mslp_c4_v[:] = mslp_c4
mslp_c5_v[:] = mslp_c5
mslp_c6_v[:] = mslp_c6
mslp_c7_v[:] = mslp_c7
#mslp_c8_v[:] = mslp_c8
#mslp_c9_v[:] = mslp_c9
#mslp_c10_v[:] = mslp_c10
#mslp_c11_v[:] = mslp_c11
#mslp_c12_v[:] = mslp_c12
#mslp_c13_v[:] = mslp_c13


#description
f.description = 'Mean sea level pressure (ERA-Interim) at dates where medoids are at TNn in DJF.'
f.history = 'Created 24/08/2017'
f.source = 'Global mslp data from raijin.nci.org.au:/g/data1/ub4/erai/netcdf/6hr/atmos/oper_an_ml/v01/mslp/'
#close
f.close()




