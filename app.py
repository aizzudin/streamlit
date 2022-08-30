import streamlit as st
import pandas as pd
import numpy as np

#Write title
st.title('My First App')

#Sources variables
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

#Define loading function
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

#Loading data
data_load_state = st.text('Loading data...')
data = load_data(1000)
data_load_state = st.text('Done using St cache')

#Showing raw data
#Use toggle
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

#Drawing a histogram
st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

#Plot data on map
#Filter result with a slider
hour_to_filter = st.slider('hour', 0, 23, 11) #min:0, max:23, default:11
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Maps of all pickups at {hour_to_filter}:00')
st.map(filtered_data) 