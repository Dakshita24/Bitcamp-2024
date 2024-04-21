'''
import openmeteo_requests
import matplotlib.pyplot as plt
import requests_cache
import pandas as pd
import numpy as np
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)


latitude = float(input("Enter latitude: "))
longitude = float(input("Enter longitude: ")) 

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://climate-api.open-meteo.com/v1/climate"
params = {
	"latitude": latitude,
    "longitude": longitude,
	"start_date": "2025-01-01",
	"end_date": "2050-12-31",
	"models": ["CMCC_CM2_VHR4", "FGOALS_f3_H", "HiRAM_SIT_HR", "MRI_AGCM3_2_S", "EC_Earth3P_HR", "MPI_ESM1_2_XR", "NICAM16_8S"],
	"daily": "temperature_2m_max"
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# Process daily data. The order of variables needs to be the same as requested.
daily = response.Daily()
daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()

daily_data = {"date": pd.date_range(
	start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
	end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = daily.Interval()),
	inclusive = "left"
)}
daily_data["temperature_2m_max"] = daily_temperature_2m_max

daily_dataframe = pd.DataFrame(data = daily_data) ''' 



import openmeteo_requests
import numpy as np
import requests_cache
import pandas as pd
from retry_requests import retry 
import matplotlib.pyplot as plt
import time

f = open("states.csv", "r")
data_list = []
for x in f:
    data_list.append(x.split())
print(data_list)
for i in data_list:
    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    latitude = float(i[1])
    longitude = float(i[2]) 
    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://climate-api.open-meteo.com/v1/climate"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": "2025-01-01",
        "end_date": "2050-12-31",
        "daily": "temperature_2m_mean"
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]
    #print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
    #print(f"Elevation {response.Elevation()} m asl")
    #print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
    #print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

    # Process daily data. The order of variables needs to be the same as requested.
    daily = response.Daily()
    daily_temperature_2m_mean = daily.Variables(0).ValuesAsNumpy()

    daily_data = {"date": pd.date_range(
        start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
        end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
        freq = pd.Timedelta(seconds = daily.Interval()),
        inclusive = "left"
    )}
    daily_data["temperature_2m_mean"] = daily_temperature_2m_mean

    daily_dataframe = pd.DataFrame(data = daily_data)
    #print(daily_dataframe)


    plt.plot(daily_dataframe['date'], daily_dataframe['temperature_2m_mean'])
    plt.xlabel('Date')
    plt.ylabel('temperature_2m_mean')
    plt.title('Climate change')
    plt.xticks(rotation=45)
    plt.tight_layout()
    #Test
    npxs = np.array(daily_dataframe['date'])
    npys = np.array(daily_dataframe['temperature_2m_mean'])


    def Pearson_correlation(X,Y):
        if len(X)==len(Y):
            Sum_xy = sum((X-np.mean(X))*(Y-np.mean(Y)))
            Sum_x_squared = sum((X-np.mean(X))**2)
            Sum_y_squared = sum((Y-np.mean(Y))**2)      
            corr = Sum_xy / np.sqrt(Sum_x_squared * Sum_y_squared)
        return corr
    
    npxs_int = []
    for j in npxs:
        #print(j)
        npxs_int.append(int(j.year))
    print(i[0] + " " + str(Pearson_correlation(npxs_int, npys)))
    time.sleep(0.1)

    #EndTest
    # Show the plot
    #plt.show()



'''
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
import numpy as np
import matplotlib.pyplot as plt

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# Accept latitude and longitude from user input
latitude = float(input("Enter latitude: "))
longitude = float(input("Enter longitude: "))

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://flood-api.open-meteo.com/v1/flood"
params = {
    "latitude": latitude,
    "longitude": longitude,
    "daily": "river_discharge",
    "forecast_days": 183
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# Process daily data. The order of variables needs to be the same as requested.
daily = response.Daily()
daily_river_discharge = daily.Variables(0).ValuesAsNumpy()

daily_data = {"date": pd.date_range(
    start=pd.to_datetime(daily.Time(), unit="s", utc=True),
    end=pd.to_datetime(daily.TimeEnd(), unit="s", utc=True),
    freq=pd.Timedelta(seconds=daily.Interval()),
    inclusive="left"
)}
daily_data["river_discharge"] = daily_river_discharge

daily_dataframe = pd.DataFrame(data=daily_data)

# Plot the data
plt.plot(daily_dataframe['date'], daily_dataframe['river_discharge'])
plt.xlabel('Date')
plt.ylabel('River Discharge')
plt.title('Daily River Discharge')
plt.xticks(rotation=45)
plt.tight_layout()

#Test
npxs = np.array(daily_dataframe['date'])
npys = np.array(daily_dataframe['river_discharge'])


def Pearson_correlation(X,Y):
   if len(X)==len(Y):
       Sum_xy = sum((X-np.mean(X))*(Y-np.mean(Y)))
       Sum_x_squared = sum((X-np.mean(X))**2)
       Sum_y_squared = sum((Y-np.mean(Y))**2)      
       corr = Sum_xy / np.sqrt(Sum_x_squared * Sum_y_squared)
   return corr
npxs_int = []
for i in npxs:
    print(i)
    npxs_int.append(int(i.year))
print(Pearson_correlation(npxs_int, npys))

#EndTest
# Show the plot
plt.show()

'''