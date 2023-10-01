import pandas as pd;
import numpy as np

#this is for import the .xlsx file in the python
df = pd.read_excel('C:/Users/dhvani patel/Desktop/Dhvani/Trainity Assignments/Project 8/Call_Volume_Trend_Analysis.xlsx');

#for this I applied the group by to calculate the total calls made in the every time bucket as well as I used reset index and name that as Count_Calls to the second column which is generated
count_call = df.groupby('Time_Bucket')['Time_Bucket'].count().reset_index(name='Count_Calls');

#desired abandon rate I want is 10%
desired_abandon_rate = 0.10

#Formula to count minimum agents required in each Time_Bucket
count_call['Minimum_agents'] = np.floor((count_call['Count_Calls'] * (desired_abandon_rate)) / (1 - (desired_abandon_rate))).astype(int)

#print the output
print(count_call)