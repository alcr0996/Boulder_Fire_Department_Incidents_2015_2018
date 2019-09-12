import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
import plotting_help_functions as phf

df = pd.read_csv('data/BFD_fire_stations.csv')
df_pair = df[['Response_Time', 'fire_norm_time_per_dist',
            'ELAPSEDENROUTE1STSCENEFIREMIN']].copy()
fig, ax = plt.subplots()
pair_plot = sns.pairplot(df_pair, kind = 'reg', dropna=True)