df = pd.read_csv('data/boulder_response_times.csv')

# drop data from 2019 because it is not complete
df = df[df['RESPONSEYEAR'] != 2019]

# Drop all rows with zeros in 'lat' or 'long'.
df = df[(df[['lat','long']] != 0).all(axis=1)]

# Drop all rows concerning ambulances
df.drop(list(df.filter(regex = 'AMR')), axis = 1, inplace = True)

# Haversine is a function to calculate distance between points
# on a sphere.
def haversine(row, lat1, lon1, lat2, lon2):

    R = 3959.87433 # this is in miles.  For Earth radius in kilometers use 6372.8 km

    lat1 = radians(row[lat1])
    lat2 = radians(row[lat2])
    dLat = radians(lat2 - lat1)
    dLon = radians(row[lon2] - row[lon1])

    a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
    c = 2*asin(sqrt(a))

    return R * c

# Create column with distance in miles between fire station and incident using haversine
df["fire_ass_to_loc"] = response_data.apply(haversine, 
                                                    args=('fire_lat_ass', 'fire_long_ass',
                                                    'lat', 'long'), axis=1)

# Create columns with time enroute in hours
df['ELAPSEDENROUTE1STSCENEFIREHR'] = df['ELAPSEDENROUTE1STSCENEFIREMIN']/60

# Normalize distance over time
df["fire_norm_mile_per_hr"]= df['fire_ass_to_loc'] / df['ELAPSEDENROUTE1STSCENEFIREHR']

# Create columns with time over distance
df["fire_norm_time_per_dist"]= df['ELAPSEDENROUTE1STSCENEFIREHR'] / df['fire_ass_to_loc']

# Some columns created for Mapping
def program_area_icons(df):
    if df['PROGRAMAREA'] == 'Fire':
        return 'fire'
    elif df['PROGRAMAREA'] == 'Rescue':
        return 'flag'
    elif df['PROGRAMAREA'] == 'EMS':
        return 'plus-sign'
    elif df['PROGRAMAREA'] == 'Hazmat':
        return 'warning-sign'
    elif df['PROGRAMAREA'] == 'Mutual Aid':
        return 'user'
    else:
        return 'asterisk'
df["response_icon"] = df.apply(program_area_icons, axis=1)

def incident_year(df):
    if df['RESPONSEYEAR'] == 2015:
        return 'red'
    elif df['RESPONSEYEAR'] == 2016:
        return 'orange'
    elif df['RESPONSEYEAR'] == 2017:
        return 'green'
    elif df['RESPONSEYEAR'] == 2018:
        return 'darkblue'
    elif df['RESPONSEYEAR'] == 2019:
        return 'darkpurple'
    else:
        return 'gray'
df["year_color"] = df.apply(incident_year, axis=1)

# Create Datetime column to use as index and create month column
df['Datetime'] = pd.to_datetime(df['RESPONSEDATE'])
df = df.set_index('Datetime')
df["month"] = df['RESPONSEDATE'].map(lambda x: x.month)


# Add quarters for year
def quarter_of_year(df):
    if df['month'] <= 3:
        return 1
    elif df['month'] > 3 and df['month'] <= 6:
        return 2
    elif df['month'] > 6 and df['month'] <= 9:
        return 3
    elif df['month'] > 9 and df['month'] <= 12:
        return 4

df["quarter"] = df.apply(quarter_of_year, axis=1)

# Round data to 6 decimal places
df = df.round(6)

# To csv
df.to_csv('data/BFD_fire.csv')