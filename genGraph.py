import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

def generateGraph():
    # ingest csv
    df = pd.read_csv('/opt/jericho-flask/traveltime/traveltime.csv')
    df['DATE_CONVERTED'] = pd.to_datetime(df['DATE'], format='%Y-%m-%d')
    df['LEAVE_TIME_CONVERTED'] = pd.to_datetime(df['LEAVE_TIME'], format='%I:%M%p')
    df['ARRIVE_TIME_CONVERTED'] = pd.to_datetime(df['ARRIVE_TIME'], format='%I:%M%p')


    plt.style.use('seaborn-v0_8-darkgrid')
    # to home = orange, to work = blue

    df_to_work = df[df['DIRECTION'] == 'Work']
    df_to_home = df[df['DIRECTION'] == 'Home']

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().yaxis.set_major_formatter(mdates.DateFormatter('%I:%M%p'))

    plt.scatter(df_to_work['DATE_CONVERTED'], df_to_work['LEAVE_TIME_CONVERTED'], color='cornflowerblue', alpha=0.8)
    plt.scatter(df_to_work['DATE_CONVERTED'], df_to_work['ARRIVE_TIME_CONVERTED'], color='cornflowerblue', alpha=0.8)

    plt.scatter(df_to_home['DATE_CONVERTED'], df_to_home['LEAVE_TIME_CONVERTED'], color='coral', alpha=0.8)
    plt.scatter(df_to_home['DATE_CONVERTED'], df_to_home['ARRIVE_TIME_CONVERTED'], color='coral', alpha=0.8)

    plt.title('Departure and Arrival Times by Date')

    plt.gcf().autofmt_xdate()
    plt.savefig('/opt/jericho-flask/traveltime/charts/generated.png')
    plt.clf()
