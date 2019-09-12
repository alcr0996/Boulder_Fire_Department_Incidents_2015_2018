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

# Setting up KDE plot - Day of Week vs. Hours
x = df['RESPONSEDOW']
y = df['RESPONSEHOUR']
phf.kde_plot(x, y, ylabel = 'Hour of the Day',
            xlabel = 'Day of the Week')

# Setting up KDE plot - Year vs. Month
x = df['RESPONSEYEAR']
y = df['month']
phf.kde_plot(x, y, ylabel = 'Month(January - December)',
            xlabel = 'Year (2015-2018)')