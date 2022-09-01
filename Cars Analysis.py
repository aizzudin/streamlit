import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Retrieving data
url = 'https://drive.google.com/file/d/15EX86AjdObYhay_I9NQf1_M4f_Tfdq2C/view?usp=sharing'
url = 'https://drive.google.com/uc?id=' + url.split('/')[-2]
df = pd.read_csv(url)

#CLEANING DATA
#Create Brand column
df['Car Name'] = df['Car Name'].str.replace('Land Rover', 'Land-Rover')
df['Car Name'] = df['Car Name'].str.replace('Aston Martin', 'Aston-Martin')
df['Car Name'] = df['Car Name'].str.replace('Rolls Royce', 'Rolls-Royce')
df['Car Name'] = df['Car Name'].str.replace('Strom Motors', 'Strom-Motors')
df['Brand'] = df['Car Name'].str.split(' ').str[0]

#Clean Car Name column
df['Car Name'] = [" ".join(x) for x in df['Car Name'].str.split(' ').str[1:]]

#Clean Reviews Count column
reviews = df['Reviews Count'].str.replace(' reviews', '')
reviews = reviews.str.replace(' review', '')
df['Reviews Count'] = reviews

#Replace NaN with 2 and change from float to int in Seating Capacity column
df['Seating Capacity'].fillna(2, inplace=True)
df['Seating Capacity'] = df['Seating Capacity'].apply(lambda x: int(x))

#Convert Starting and Ending Prie to USD
df['Starting Price'] = df['Starting Price'].map(lambda x: x/80)
df['Ending Price'] = df['Ending Price'].map(lambda x: x/80)


#GROUPING BY BRANDS AND MEAN
df_mean = df.groupby(['Brand']).mean()


#Show Graph
# plt.figure(figsize=[12,8])
# index = df_mean.index
# start_p = df_mean['Starting Price']
# end_p = df_mean['Ending Price']

# plt.barh(range(len(index)), width=[h-b for h, b in zip(start_p, end_p)], left=start_p, align='center')
# plt.yticks(range(len(index)), index)
# plt.grid()
# plt.title("Average Price Range of Car Brands ($)")
# plt.xlim(0,100000)

# plt.tight_layout()
# plt.show()

#TITLE
st.title("Cars Explorer")

#METRICS
col1, col2, col3 = st.columns(3)
col1.metric("Brand Listed", len(df_mean.index))
col2.metric("Cars Listed", len(df))
col3.metric("Average Rating", float("{:.2f}".format(df['Rating'].mean())))

#RAW DATA
st.subheader('Raw Data')
st.dataframe(df)

#Graph 1
fig, ax = plt.subplots(range(len(index)), width=[h-b for h, b in zip(start_p, end_p)], left=start_p, align='center')
ax.barh()
st.pyplot(fig)

