import pandas as pd;
import matplotlib.pyplot as plt 

#this is for import the .xlsx file in the python
df = pd.read_excel('C:/Users/dhvani patel/Desktop/Dhvani/Trainity Assignments/Project 8/Call_Volume_Trend_Analysis.xlsx');

#for this I applied the group by to calculate the total calls made in the every time bucket as well as I used reset index and name that as Count_Calls to the second column which is generated
count_call = df.groupby('Time_Bucket')['Time_Bucket'].count().reset_index(name='Count_Calls');

#This is to sort the data in descending order reference to the count of calls
count_call = count_call.sort_values(by='Count_Calls', ascending=False)

#to provide the custome colors to the bars
custom_colors = ['#013220', '#008000', '#006400', '#2e8b57', '#3cb371','#32cd32','#00fa9a','#90ee90','#007f66','#3b7a57','#3fff00'] 

#to set the size of the figure
plt.figure(figsize=(9, 5))

#insert the bar graph from the matplotlib which will have Time_Bucket on X axis and Count_Calls on Y axis as well as colors according to custome_colors variable
bars = plt.bar(count_call['Time_Bucket'], count_call['Count_Calls'], color=custom_colors)

#Give the lable to the X axis
plt.xlabel('Time_Bucket')

#Give the lable to the Y axis
plt.ylabel('Count_Calls')

#Give the title to the bar graph
plt.title('Call Volume Trend Analysis by Time Bucket')

#Rotate the data on the X axis at 45 degree
plt.xticks(rotation=45)

#give the data lables on each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), ha='center', va='bottom')

#every element of the data fits perfectly after using this
plt.tight_layout()

#To display the graph
plt.show()

# print(count_call)