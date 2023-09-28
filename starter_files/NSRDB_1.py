import pandas as pd
import numpy as np
import sys, os
# Declare all variables as strings. Spaces must be replaced with '+', i.e., change 'John Smith' to 'John+Smith'.
# Define the lat, long of the location and the year
year = 2017
# You must request an NSRDB api key from the link above
api_key = 'npIQd9rtanUEaGsavnRButawXj5lSh0X9OgAIc7o'
# Set the attributes to extract (e.g., dhi, ghi, etc.), separated by commas.
# attributes = 'ghi,dhi,dni,wind_speed_10m_nwp,surface_air_temperature_nwp,solar_zenith_angle'
# attributes = 'air_temperature,cloud_type,fill_flag,ghi,relative_humidity,surface_pressure,total_precipitable_water,wind_speed'
#attributes ='air_temperature, clearsky_dhi, clearsky_dni, clearsky_ghi, cloud_type, dew_point, dhi, dni, fill_flag, ghi, relative_humidity, solar_zenith_angle, surface_albedo, surface_pressure, total_precipitable_water, wind_direction, wind_speed'
attributes = ''
# Choose year of data
year = '2017'
# Set leap year to true or false. True will return leap day data if present, false will not.
leap_year = 'false'
# Set time interval in minutes, i.e., '30' is half hour intervals. Valid intervals are 30 & 60.
interval = '30'
# Specify Coordinated Universal Time (UTC), 'true' will use UTC, 'false' will use the local time zone of the data.
# NOTE: In order to use the NSRDB data in SAM, you must specify UTC as 'false'. SAM requires the data to be in the
# local time zone.
utc = 'false'
# Your full name, use '+' instead of spaces.
your_name = 'Ablimit+Aili'
# Your reason for using the NSRDB.
reason_for_use = 'Research'
# Your affiliation
your_affiliation = 'CU+Boulder'
# Your email address
your_email = 'Ablimit.Aili@colorado.edu'
# Please join our mailing list so we can keep you up-to-date on new developments.
mailing_list = 'false'

data = pd.read_csv("C:\\Users\\aatmm\\Dropbox\\Python\\USMAP_3000points.csv") 
Y = data.lon
X = data.lat
print(Y[25])
print(len(Y))


for j in range(24, len(Y)):
    lon = Y[j]
    lat = X[j]
    # Declare url string
    # url = 'http://developer.nrel.gov/api/solar/nsrdb_0512_download.csv?wkt=POINT({lon}%20{lat})&names={year}&leap_day={leap}&interval={interval}&utc={utc}&full_name={name}&email={email}&affiliation={affiliation}&mailing_list={mailing_list}&reason={reason}&api_key={api}&attributes={attr}'.format(year=year, lat=lat, lon=lon, leap=leap_year, interval=interval, utc=utc, name=your_name, email=your_email, mailing_list=mailing_list, affiliation=your_affiliation, reason=reason_for_use, api=api_key, attr=attributes)
    url = 'http://developer.nrel.gov/api/solar/nsrdb_psm3_download.csv?wkt=POINT({lon}%20{lat})&names={year}&leap_day={leap}&interval={interval}&utc={utc}&full_name={name}&email={email}&affiliation={affiliation}&mailing_list={mailing_list}&reason={reason}&api_key={api}&attributes={attr}'.format(year=year, lat=lat, lon=lon, leap=leap_year, interval=interval, utc=utc, name=your_name, email=your_email, mailing_list=mailing_list, affiliation=your_affiliation, reason=reason_for_use, api=api_key, attr=attributes)
    
    # Return just the first 2 lines to get metadata:
    info = pd.read_csv(url, nrows=1)
    # See metadata for specified properties, e.g., timezone and elevation
    timezone, elevation = info['Local Time Zone'], info['Elevation']
    # View metadata
    # info
    
    # Return all but first 2 lines of csv to get data:
    # df = pd.read_csv('http://developer.nrel.gov/api/solar/nsrdb_psm3_download.csv?wkt=POINT({lon}%20{lat})&names={year}&leap_day={leap}&interval={interval}&utc={utc}&full_name={name}&email={email}&affiliation={affiliation}&mailing_list={mailing_list}&reason={reason}&api_key={api}&attributes={attr}'.format(year=year, lat=lat, lon=lon, leap=leap_year, interval=interval, utc=utc, name=your_name, email=your_email, mailing_list=mailing_list, affiliation=your_affiliation, reason=reason_for_use, api=api_key, attr=attributes), skiprows=2)
    df = pd.read_csv(url)
    # Set the time index in the pandas dataframe:
    # df = df.set_index(pd.date_range('1/1/{yr}'.format(yr=year), freq=interval+'Min', periods=525600/int(interval)))
    
    # take a look
    # print 'shape:',df.shape
    print('shape:',df.shape)
    df.head()
#    print(df.columns.values)
    # Print column names
#    lon = info.Longitude.values
#    lon = lon[0]
#    lat = info.Latitude.values
#    lat = lat[0]
    df.to_csv('C:\\Users\\aatmm\\OneDrive\\Documents\\Nrel_Weather_Data3\\1deg_res\\{lat}_{lon}_{year}.csv'.format(lat = lat, lon = lon, year = year), index=False)
    # info.to_csv('C:\\Users\\aatmm\\OneDrive\\Documents\\Nrel_Weather_Data3\\Single files\\{lat}_{lon}.csv'.format(lat = lat, lon = lon))
    print(j)
    
#    df = pd.read_csv(url)

