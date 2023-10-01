import pandas as pd;
import numpy as np;

#import the excel file
df = pd.read_excel('C:/Users/dhvani patel/Desktop/Dhvani/Trainity Assignments/Project 8/Call_Volume_Trend_Analysis.xlsx');

#count the total calls per month
Day_Total_calls = df['Time_Bucket'].count()

#Total working days in month in which 6 days a week means 6*4 =24 and each employee take unplanned leaves of 4 days on an average so we consider 20 days a month
Total_working_days_in_month = 20 

#Total calls at night from 9pm to 9am which is 30 outof 100 means 30 percent of the days calls means calculated a total days calls and find the 30% of it to get the total calls at night in a month
Night_Total_calls = Day_Total_calls * 0.30

#agent working hours per day which is 9 hour job including 1.5 hour for lunch and snacks and outof 9-1.5 = 7.5 hours they spent 60% of it on calls with customers
Agent_working_hours_per_day = 7.5*0.60

#maximum abandon rate we want is 10%
maximum_abandon_rate = 0.10

#added the night time bucket for a month according to the data given for the 30 calls 
Night_time_bucket = {'Time_Bucket' : ['21-22','22-23','23-24','24-1','1-2','2-3','3-4','4-5','5-6','6-7','7-8','8-9'],
                     'Count_Calls':[Night_Total_calls*0.03,Night_Total_calls*0.03,Night_Total_calls*0.02,Night_Total_calls*0.02,Night_Total_calls*0.01,Night_Total_calls*0.01,Night_Total_calls*0.01,Night_Total_calls*0.01,Night_Total_calls*0.03,Night_Total_calls*0.04,Night_Total_calls*0.04,Night_Total_calls*0.05]}

#convert the above object into the dataframe
Night_df = pd.DataFrame(Night_time_bucket)

#used groupby to count the total calls per month for each bucket
Total_calls_per_bucket = df.groupby('Time_Bucket')['Time_Bucket'].count().reset_index(name='Count_Calls')

#combine the days and night bucket in one dataframe
Day_Total_Bucket = pd.concat([Total_calls_per_bucket,Night_df], ignore_index=True)
Day_Total_Bucket = pd.DataFrame(Day_Total_Bucket)

#find the minimum agents required to maintain the maximum abandon rate at 10% per day
Day_Total_Bucket['Minimum_agents'] = np.int_(Day_Total_Bucket['Count_Calls']*maximum_abandon_rate/((1-maximum_abandon_rate)*Agent_working_hours_per_day*Total_working_days_in_month))


# print(Total_calls_per_bucket)
# print(Day_Total_calls)
# print(Night_Total_calls)
# print(Night_df)

#printed the output
print(Day_Total_Bucket.head(30))