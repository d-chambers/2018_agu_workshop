"""
A library for analogizing Berkley temperature data. Created in the best
practices for open-source software development at AGU-2018.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import requests


def _generate_berkley_earth_location_url(location: str) -> str:
    " "
    base = 'http://berkeleyearth.lbl.gov/auto/Regional/TAVG/Text/'
    location = f'{location.lower()}-TAVG-Trend.txt'
    # Download the content of the URL
    return base + location

def download_data(location: str, path=None) -> str:
    url = _generate_berkley_earth_location_url(location)
    response = requests.get(url)
    # Save it to a file
    if path:
        with open(path, 'w') as fi:
            fi.write(response.text)
    return response.text


def load_data(path_or_str: str):
    path = Path(path_or_str)
    try:
        if path.exists():
            return np.loadtxt("data.txt", comments="%")
    except OSError:
        pass
    pstring = [x.rstrip().split() for x in path_or_str.splitlines()
               if not x.startswith('%') and x.rstrip()]
    return np.array(pstring).astype(float)


# In[79]:


# test for loading text


# Extract the monthly temperature anomaly and calculate an approximate "decimal year" to use in plotting.

# In[4]:





# Plot the data so we can see what it's like.

# In[5]:

decimal_year = data[:, 0] + 1 / 12 * (data[:, 1] - 1)
temp_anomaly = data[:, 2]
plt.figure(figsize=(10, 6))
plt.title("Temperature anomaly for Australia")
plt.plot(decimal_year, temp_anomaly)
plt.xlabel('year')
plt.ylabel('temperature anomaly (C)')
plt.grid()
plt.xlim(decimal_year.min(), decimal_year.max())


# The data are kind of noisy at this scale so let's calculate a 12-month moving average for a smoother time series.

# In[80]:


def moving_avg(temp_anomaly):
    moving_avg = np.full(temp_anomaly.size, np.nan)
    for i in range(6, moving_avg.size - 6):
        moving_avg[i] = np.mean(temp_anomaly[i - 6:i + 6])


# In[7]:


plt.figure(figsize=(10, 6))
plt.title("Temperature anomaly for Australia")
plt.plot(decimal_year, temp_anomaly, label="anomaly")
plt.plot(decimal_year, moving_avg, label="12-month moving average", linewidth=3)
plt.xlabel('year')
plt.ylabel('temperature anomaly (C)')
plt.legend()
plt.grid()
plt.xlim(decimal_year.min(), decimal_year.max())




