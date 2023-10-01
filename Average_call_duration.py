import pandas as pd;

#this is for import the .xlsx file in the python
df = pd.read_excel('C:/Users/dhvani patel/Desktop/Dhvani/Trainity Assignments/Project 8/Call_Volume_Trend_Analysis.xlsx');

#Convert the 'Duration(hh:mm:ss)' into timedelts format so that we can perform various operations like sum, average etc. on the time column AND used astype() to convert the datetime column in string bcz timedelta do noy accept the datetime format
df['Duration(hh:mm:ss)'] = pd.to_timedelta(df['Duration(hh:mm:ss)'].astype(str));

#Applied the filter on the column name Call_Status bcz I want the average duration for the received call not abandon call
filtered_df = df[df['Call_Status'] != 'abandon']

#generate the new dataframe in which I used the filtered_df and applied a group by and reset the index to get the separated column
average_duration = filtered_df.groupby('Time_Bucket')['Duration(hh:mm:ss)'].mean().reset_index();

#This will generate the new AVG_duration column in the average_duration dataframe by formating the timedelta to hh:mm:ss using the lambda function
average_duration['AVG_duration'] = average_duration['Duration(hh:mm:ss)'].dt.total_seconds().apply(lambda x: '{:02}:{:02}:{:02}'.format(int(x // 3600), int((x % 3600) // 60), int(x % 60)));

#This will drop the column name Duration(hh:mm:ss)
average_duration = average_duration.drop(columns=['Duration(hh:mm:ss)']);

#print the resulting dataframe
print(average_duration);