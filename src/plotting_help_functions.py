import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import datetime as dt

# Edit MatPlotLib Parameters
plt.rcParams.update({'font.size': 20})
plt.style.use('ggplot')

# Bar Plot
def bar_plot(x, y, ax, title=False, xlabel=False, ylabel=False):
    sns.barplot(x=x, y=y, ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.tight_layout()
    plt.savefig('images/'+title+'.png')
    return ax

# Line Plot
def line_plot(x, y, ax, title=False, xlabel=False, ylabel=False):
    sns.lineplot(x=x, y=y, ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.tight_layout()
    plt.savefig('images/'+title+'.png')
    return ax


# Plotting function built for time interval vs. response time
def kde_plot(x, y, xlabel=False, ylabel=False):
    ax = sns.set(style="ticks")
    a = sns.jointplot(x, y, kind="kde", color='brown',xlim=(-.5,6.5), ylim=(-.5,23.5))
    a.set_axis_labels(xlabel, ylabel, fontsize=18)
    name = 'kde_plot'
    plt.tight_layout()
    plt.savefig('images/'+name+'.png')
    return ax