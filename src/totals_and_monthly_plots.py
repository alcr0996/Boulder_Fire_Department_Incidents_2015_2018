import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
import plotting_help_functions as phf

# Edit MatPlotLib Parameters
plt.rcParams.update({'font.size': 20})
plt.style.use('ggplot')

# Import data
df = pd.read_csv('data/BFD_fire.csv')

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday']

# Setting up Year vs Total Incidents Plot
group_year = df.groupby('RESPONSEYEAR')
incidents_per_year = group_year['ID'].count().reset_index()
x = incidents_per_year['RESPONSEYEAR']
height = incidents_per_year['ID']
fig, ax = plt.subplots()
phf.bar_plot(x, height, ax, 'Incidents per Year', 'Year',
                        'Total Incidents')

# Average Incidents per month plot
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']  
group_month = df.groupby('month')
incidents_per_month = group_month['ID'].count().reset_index()
x = incidents_per_month['month']
height = incidents_per_month['ID']/4
fig, ax = plt.subplots()
phf.bar_plot(x, height, ax, 'Incidents per Month (Avg)', 'Month',
                        'Total Incidents')
ax.set_xticklabels(months)

# Avg Incidents per Response Area
group_yr_prog_area = df.groupby(['RESPONSEYEAR','PROGRAMAREA'])
incidents_yr_prog_area = group_yr_prog_area['ID'].count().reset_index()
x = incidents_yr_prog_area['PROGRAMAREA']
height = incidents_yr_prog_area['ID']
fig, ax = plt.subplots()
phf.bar_plot(x, height, ax, 'Average Incidents per Program Area (2015-2018)', 'Program Area',
                        'Total Incidents (Avg)')

# % Program area per year per month
group_month_area = df.groupby(['month','PROGRAMAREA'])
group_month = df.groupby('month')['ID'].count()
incidents_month_area_percent = group_month_area['ID'].count()/group_month
height = incidents_month_area_percent
x = height.index
fig, ax = plt.subplots()
phf.bar_plot(x, height, ax, 'Percent Incidents per Program Area', 'Month/Program Area',
                        'Total Incidents (Avg)')
plt.xticks(rotation=90)

# Count Program area per month
group_month_area = df.groupby(['month','PROGRAMAREA'])
incidents_year_month_area = group_month_area['ID'].count()
height = incidents_year_month_area
x = height.index
fig, ax = plt.subplots()
phf.bar_plot(x, height, ax, 'Average Incidents per Program Area', 'Month/Program Area',
                        'Average Total Incidents')
plt.xticks(rotation=90)


if __name__=="__main__":

# Edit MatPlotLib Parameters
        # plt.rcParams.update({'font.size': 20})
        

# Import data
        # df = pd.read_csv('data/BFD_fire.csv')

        # group_month_area = df.groupby(['month','PROGRAMAREA'])
        # incidents_year_month_area = group_month_area['ID'].count()
        # height = incidents_year_month_area
        # x = height.index
        # fig, ax = plt.subplots()
        # phf.bar_plot(x, height, ax, 'Average Incidents per Program Area', 'Month/Program Area',
        #                 'Average Total Incidents')
        # plt.xticks(rotation=90)