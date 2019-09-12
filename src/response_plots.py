import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
import plotting_help_functions as phf

plt.rcParams.update({'font.size': 20})
df = pd.read_csv('data/BFD_fire_stations.csv')

# Average Response Time by Hour
hour_group = df.groupby('RESPONSEHOUR')
fig, ax = plt.subplots()
y = hour_group['Response_Time'].mean()
x = y.index
err = hour_group['Response_Time'].std()
sns.barplot(x, y, yerr = err)
ax.set_title('Average Response Time by Hour')
ax.set_ylabel('Time to depart station(min)')
ax.set_xlabel('Hour of the Day')
plt.savefig('images/'+'avg_resp_by_hour'+'.png')

# Count of # of Responses by Station
station_group = df.groupby('LOCATIONATASSIGNFIRE')
fig, ax = plt.subplots()
y = station_group['ID'].count()
x = y.index
phf.bar_plot(x, y, ax, title='Total Incidents Responded to by Station',
             xlabel='Station ID', ylabel='Incident Count')
plt.xticks(rotation=90)

# Avg. Response Time per Station
day_group = df.groupby('LOCATIONATASSIGNFIRE')
fig, ax = plt.subplots()
y = day_group['Response_Time'].mean()
x = y.index
phf.bar_plot(x, y, ax, title='Average Response Time per Station',
              xlabel='Station ID', ylabel='Average Response Time')
plt.xticks(rotation=90)

# Most common locations to respond to:
location_group = df.groupby(['lat','long'])
fig, ax = plt.subplots()
y = location_group['ID'].count().sort_values(ascending=False).head(10)
print(y.sum())
x = np.arange(1,11,1)
phf.bar_plot(x, y, ax, title='Most Commonly Responded to Locations',
             xlabel='Location', ylabel='Response Count')


if __name__=="__main__":
    plt.rcParams.update({'font.size': 20})
    df = pd.read_csv('data/BFD_fire_stations.csv')
    # df.round(6)