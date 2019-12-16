# -*- coding: utf-8 -*-
"""
Matt Girman

Step Tracker Analysis
11/25/19
"""

import statistics
import matplotlib.pyplot as plt
import numpy as np

#Function for plotting the data for the user's choice of month
def user_choice(names, months, choice):
    #Create array of steps taken and array of days for the x axis
    y = months[choice]
    x = np.arange(1, len(y)+1)
    
    #Plot steps taken for each day
    plt.bar(x,y)
    plt.xlabel('Day')
    plt.ylabel('Steps Taken')
    plt.title(names[choice-1])
    plt.show()
    
    #Create array of miles walked each day
    y_miles = []
    for k in y:
        y_miles.append(k * 2.4 / 5280)
    
    #Plot miles walked
    plt.bar(x,y_miles)
    plt.xlabel('Day')
    plt.ylabel('Miles Walked')
    plt.title(names[choice-1])
    plt.show()



#Declare some arrays
steps = []
avsteps = []
miles = []
names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
         'Oct', 'Nov', 'Dec']


# Read each line from the file and save as an array
with open('steps.txt', mode='r') as file:
    for x in file.readlines():
        steps.append(int(x))
        
#Create dicitonary of steps for each month
months = {1: steps[0:31],
          2: steps[31:59],
          3: steps[59:90],
          4: steps[90:120],
          5: steps[120:151],
          6: steps[151:181],
          7: steps[181:212],
          8: steps[212:243],
          9: steps[243:273],
          10: steps[273:304],
          11: steps[304:334],
          12: steps[334:365]}

#Create an array of the average steps for each month and display it
i = 0
print('Month     Avg Steps')
print('-------------------')
for x in months:
    avsteps.append(statistics.mean(months[x]))
    print(names[i] +'       ' +str(format(avsteps[i], '.2f')))
    i += 1
    
#Plot average steps taken
plt.bar(names, avsteps)
plt.xlabel('Month')
plt.ylabel('Average Steps per Day')
plt.title('Steps Taken')
plt.show()

#Convert steps to miles and display
j = 0
print('Month     Avg Miles')
print('-------------------')
for x in avsteps:
    miles.append(x * 2.4 / 5280)
    print(names[j] +'       ' +str(format(miles[j], '.2f')))
    j += 1
    
#Plot average miles walked
plt.bar(names, miles)
plt.xlabel('Month')
plt.ylabel('Average Miles per Day')
plt.title('Miles Walked')
plt.show()

#Ask the user for a month. If the user enters an invalid month, it asks again.

choice = 0

while choice < 1 or choice > 12:
    choice = int(input("For which month would you like to see the step data? Enter" +
                       " a number (i.e. 1 for January, 2 for February, etc) "))
    
    if choice < 1 or choice > 12:
        print("Please enter a valid month.")

#Call function for displaying data for the user's month
user_choice(names, months, choice)