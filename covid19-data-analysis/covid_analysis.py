import pandas as pd 
import matplotlib.pyplot as plt 

#Load the data from John Hopkins University repository
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
df = pd.read_csv(url)

#Group the cases by data and sum the cases 
df = df.groupby(df.columns[4:]).sum().transpose()

#Convert the index to datetime
df.index = pd.to_datetime(df.index)

#Plot the time series of COVID-19 confirmed cases 
df.sum(axis=1).plot()
plt.title('Confirmed COVID-19 cases through time')
plt.show()
