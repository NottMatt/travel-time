import matplotlib.pyplot as plt
import pandas as pd

# Read CSV
df = pd.read_csv('/opt/jericho-flask/traveltime/traveltime.csv')

plt.style.use('seaborn-v0_8-darkgrid')

# Make leave time and arrive time and direction columns all lower case
df['LEAVE_TIME'] = df['LEAVE_TIME'].str.lower()
df['ARRIVE_TIME'] = df['ARRIVE_TIME'].str.lower()
df['DIRECTION'] = df['DIRECTION'].str.lower()

# Convert dates
df['DATE'] = pd.to_datetime(df['DATE'], format='%Y-%m-%d')
df['LEAVE_TIME'] = pd.to_datetime(df['LEAVE_TIME'], format='%I:%M%p')
df['ARRIVE_TIME'] = pd.to_datetime(df['ARRIVE_TIME'], format='%I:%M%p')

# Calculate trip duration in minutes and add it to the data frame
df['TRIP_DURATION'] = (df['ARRIVE_TIME'] - df['LEAVE_TIME']).dt.total_seconds() / 60.0
df = df.sort_values(['DATE', 'DAY_OF_WEEK'])

# Calculate the average trip duration by day of week for work
df_work = df[df['DIRECTION'] == 'work'].groupby('DAY_OF_WEEK')['TRIP_DURATION'].mean().reset_index()
days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri"]

# Sort the data frame by day of week:
df_work['DAY_OF_WEEK'] = pd.Categorical(df_work['DAY_OF_WEEK'], categories=days_of_week, ordered=True)
df_work = df_work.sort_values('DAY_OF_WEEK')

df_home = df[df['DIRECTION'] == 'home'].groupby('DAY_OF_WEEK')['TRIP_DURATION'].mean().reset_index()

# Sort the data frame by day of week:
df_home['DAY_OF_WEEK'] = pd.Categorical(df_home['DAY_OF_WEEK'], categories=days_of_week, ordered=True)
df_home = df_home.sort_values('DAY_OF_WEEK')

# Make a new column with short dates which are just month and day
short_dates = df['DATE'].dt.strftime('%m-%d')
df['SHORT_DATE'] = short_dates
df_home_date = df[df['DIRECTION'] == 'home'].groupby('SHORT_DATE')['TRIP_DURATION'].mean().reset_index()
df_work_date = df[df['DIRECTION'] == 'work'].groupby('SHORT_DATE')['TRIP_DURATION'].mean().reset_index()

# Create a complete date range for the all entries
date_range = pd.date_range(start=df['DATE'].min(), end=df['DATE'].max(), freq='D')
date_range_str = date_range.strftime('%m-%d')

# Merge work and home DataFrames, filling gaps with NaN
merged_df = pd.merge(df_work_date, df_home_date, on='SHORT_DATE', how='right')
merged_df.columns = ['SHORT_DATE', 'TRIP_DURATION_WORK', 'TRIP_DURATION_HOME']
merged_df = merged_df.sort_values('SHORT_DATE')

# Interpolate missing values
merged_df['TRIP_DURATION_WORK_INT'] = merged_df['TRIP_DURATION_WORK'].interpolate()
merged_df['TRIP_DURATION_HOME_INT'] = merged_df['TRIP_DURATION_HOME'].interpolate()

# generate a bar chart of df_work titled average commute to work by day and save to day_work.png
plt.bar(df_work['DAY_OF_WEEK'], df_work['TRIP_DURATION'])
plt.title('Average Commute to Work by Day')
plt.xlabel('Day of Week')
plt.ylabel('Minutes')
plt.savefig('charts/day_work.png')
plt.clf()

# generate a bar chart of the average commute to home by day and save to day_home.png
plt.bar(df_home['DAY_OF_WEEK'], df_home['TRIP_DURATION'])
plt.title('Average Commute Home by Day')
plt.xlabel('Day of Week')
plt.ylabel('Minutes')
plt.savefig('charts/day_home.png')
plt.clf()

# Generate a bar chart of average commute time by driver going to work and save to driver_work.png
df_work_driver = df[df['DIRECTION'] == 'work'].groupby('DRIVER')['TRIP_DURATION'].mean().reset_index()
plt.bar(df_work_driver['DRIVER'], df_work_driver['TRIP_DURATION'])
plt.title('Average Commute to Work by Driver')
plt.xlabel('Driver')
plt.ylabel('Minutes')
plt.savefig('charts/driver_work.png')
plt.clf()

# Generate a bar chart of average commute time by driver going home and save to driver_home.png
df_home_driver = df[df['DIRECTION'] == 'home'].groupby('DRIVER')['TRIP_DURATION'].mean().reset_index()
plt.bar(df_home_driver['DRIVER'], df_home_driver['TRIP_DURATION'])
plt.title('Average Commute Home by Driver')
plt.xlabel('Driver')
plt.ylabel('Minutes')
plt.savefig('charts/driver_home.png')
plt.clf()

# Generate line chart of commute to work by date and save to date_work.png

plt.plot(df_work_date['SHORT_DATE'], df_work_date['TRIP_DURATION'])
plt.title('Commute to Work by Date')
plt.xlabel('Date')
plt.ylabel('Minutes')
plt.xticks(rotation=35)
plt.tight_layout()
plt.savefig('charts/date_work.png')
plt.clf()

# Generate line chart of commute home by date and save to date_home.png
plt.plot(df_home_date['SHORT_DATE'], df_home_date['TRIP_DURATION'])
plt.title('Commute Home by Date')
plt.xlabel('Date')
plt.ylabel('Minutes')
plt.xticks(rotation=35)
plt.tight_layout()
plt.savefig('charts/date_home.png')
plt.clf()

# TODO: side by side bar chart of average commute time by driver going to work and home


# Set markers for non-interpolated data
plt.plot(merged_df['SHORT_DATE'], merged_df['TRIP_DURATION_WORK'], color='cornflowerblue', marker='o', label='Towards Work')
plt.plot(merged_df['SHORT_DATE'], merged_df['TRIP_DURATION_HOME'], color='coral', marker='o', label='Towards Home')

# Plot interpolated lines without markers
plt.plot(merged_df['SHORT_DATE'], merged_df['TRIP_DURATION_WORK_INT'], color='cornflowerblue')
plt.plot(merged_df['SHORT_DATE'], merged_df['TRIP_DURATION_HOME_INT'], color='coral')

plt.legend(['Towards Work', 'Towards Home'])
plt.title('Commute Time by Date')
plt.xlabel('Date')
plt.ylabel('Minutes')
plt.xticks(rotation=35)
plt.tight_layout()
plt.savefig('charts/date_both.png')
plt.clf()
