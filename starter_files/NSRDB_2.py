import pandas as pd
import requests
import time
# Declare all variables as strings. Spaces must be replaced with '+', i.e., change 'John Smith' to 'John+Smith'.
# Define the lat, long of the location and the year
year = 2017
# You must request an NSRDB api key from the link above
api_key = 'npIQd9rtanUEaGsavnRButawXj5lSh0X9OgAIc7o'
# Set the attributes to extract (e.g., dhi, ghi, etc.), separated by commas.
# attributes = 'air_temperature,cloud_type,fill_flag,ghi,dhi,dni,relative_humidity,surface_pressure,total_precipitable_water,wind_speed, solar_zenith_angle'
# attributes ='air_temperature,cloud_type,dew_point,dhi,dni,fill_flag,ghi,relative_humidity,surface_albedo,surface_pressure,total_precipitable_water,wind_direction,wind_speed'
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

# =============================================================================
# lat1, lon1 = 40.0, -105.0 # lattitude and longititude coordiantes for which weather data will be downlaoded
# lat2, lon2 = 40.1, -105.1
# lat3, lon3 = 40.2, -105.2
# lat4, lon4 = 40.3, -105.3
# lat5, lon5 = 40.4, -105.4

# # Declare url string
# url = 'http://developer.nrel.gov/api/solar/nsrdb_psm3_download.csv?wkt=MULTIPOINT({lon1}%20{lat1}%2C{lon2}%20{lat2}%2C{lon3}%20{lat3}%2C{lon4}%20{lat4}%2C{lon5}%20{lat5})&names={year}&leap_day={leap}&interval={interval}&utc={utc}&full_name={name}&email={email}&affiliation={affiliation}&mailing_list={mailing_list}&reason={reason}&api_key={api}&attributes={attr}'.format(year=year, lat1=lat1, lon1=lon1,lat2=lat2, lon2=lon2, lat3=lat3, lon3=lon3, lat4=lat4, lon4=lon4, lat5=lat5, lon5=lon5, leap=leap_year, interval=interval, utc=utc, name=your_name, email=your_email, mailing_list=mailing_list, affiliation=your_affiliation, reason=reason_for_use, api=api_key, attr=attributes)
# # Return just the first 2 lines to get metadata:
# info = pd.read_csv(url, nrows=1)
# # See metadata for specified properties, e.g., timezone and elevation
# timezone, elevation = info['Local Time Zone'], info['Elevation']
# # View metadata
# info
# # Return all but first 2 lines of csv to get data:
# df = pd.read_csv('http://developer.nrel.gov/api/solar/nsrdb_psm3_download.csv?wkt=MULTIPOINT({lon1}%20{lat1}%2C{lon2}%20{lat2}%2C{lon3}%20{lat3}%2C{lon4}%20{lat4}%2C{lon5}%20{lat5})&names={year}&leap_day={leap}&interval={interval}&utc={utc}&full_name={name}&email={email}&affiliation={affiliation}&mailing_list={mailing_list}&reason={reason}&api_key={api}&attributes={attr}'.format(year=year, lat1=lat1, lon1=lon1,lat2=lat2, lon2=lon2, lat3=lat3, lon3=lon3, lat4=lat4, lon4=lon4, lat5=lat5, lon5=lon5, leap=leap_year, interval=interval, utc=utc, name=your_name, email=your_email, mailing_list=mailing_list, affiliation=your_affiliation, reason=reason_for_use, api=api_key, attr=attributes), skiprows=2)
# 
# # Set the time index in the pandas dataframe:
# df = df.set_index(pd.date_range('1/1/{yr}'.format(yr=year), freq=interval+'Min', periods=525600*5/int(interval)))
# 
# # take a look
# # print 'shape:',df.shape
# print('shape:',df.shape)
# df.head()
# # Print column names
# print(df.columns.values)
# Data = pd.DataFrame(df)
# Data.to_csv('C:\\Users\\aatmm\\Dropbox\\Python\\{year}_{lon1}_{lat1}.csv'.format(year = year, lat1=lat1, lon1=lon1))
# =============================================================================

# data = pd.read_csv("C:\\Users\\admin\\Dropbox\\Python\\USMAP_7CSP_Plants.csv") 
data = pd.read_csv("C:\\Users\\admin\\Dropbox\\Radiative cooling project\\USMAP_3000points.csv") 
#Y = data.lon
#X = data.lat
#print(Y[5])
#print(len(Y))

X = [30.29]
Y = [-97.62]
# =============================================================================
# T = df.Temperature
# T.mean()
# =============================================================================

url = 'http://developer.nrel.gov/api/solar/nsrdb_psm3_download.json?api_key=npIQd9rtanUEaGsavnRButawXj5lSh0X9OgAIc7o'

n = 150
limit = len(Y)//n
print(limit)

for j in range(0, limit+1):
    time.sleep(2)
    if j<limit:
        WKT = ''
        for i in range(n*j,n*(j+1)):
        #    WKT+= '{Lon}%20{Alt}%2C'.format(Lon = Y[i], Alt = X[i])
            if i<n*(j+1)-1:
                WKT+=str(Y[i])+'%'+'20'+str(X[i])+'%'+'2C'
            else:
                WKT+=str(Y[i])+'%'+'20'+str(X[i])
#        print(WKT)
    else:
        WKT = ''
        for i in range(n*j,len(X)):
        #    WKT+= '{Lon}%20{Alt}%2C'.format(Lon = Y[i], Alt = X[i])
            if i<len(X)-1:
                WKT+=str(Y[i])+'%'+'20'+str(X[i])+'%'+'2C'
            else:
                WKT+=str(Y[i])+'%'+'20'+str(X[i])
#        print(WKT)
        
    payload = "names={year}&leap_day={leap}&interval={interval}&utc={utc}&full_name={name}&email={email}&affiliation={affiliation}&mailing_list={mailing_list}&reason={reason}&attributes={attr}&wkt=MULTIPOINT({WKT})".format(year=year, leap=leap_year, interval=interval, utc=utc, name=your_name, email=your_email, mailing_list=mailing_list, affiliation=your_affiliation, reason=reason_for_use, attr=attributes, WKT = WKT)
        
    headers = {'content-type': "application/x-www-form-urlencoded", 'cache-control': "no-cache"}
        
    response = requests.request("POST", url, data=payload, headers=headers)
        
    print(response.text)
    print(j)
print(i)
# =============================================================================
# WKT+=str(Y[i])+'%'+'20'+str(X[i])+'%'+'2C'
# print(WKT)
# =============================================================================

