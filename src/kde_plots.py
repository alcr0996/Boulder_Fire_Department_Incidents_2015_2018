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