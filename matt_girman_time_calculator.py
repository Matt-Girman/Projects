"""
Matthew Girman

Time Calculator
10/1/19
"""

import math

time = int(input("Enter a number of seconds: "))

if time < 60:
    print(str(time) +" seconds")
    
elif time >= 60 and time < 3600:
    minutes = time/60
    minutes = math.trunc(minutes)
    seconds = time%60
    
    print(str(minutes)+ " minutes " + str(seconds)+ " seconds")
    
elif time >= 3600 and time < 86400:
    hours = time/3600
    minutes = (time%3600)/60
    seconds = (time%3600)%60
    
    hours = math.trunc(hours)
    minutes = math.trunc(minutes)
    seconds = math.trunc(seconds)
    
    print(str(hours) + " hours " +str(minutes)+ " minutes " + str(seconds)+ " seconds")
    
else:
    days = time/86400
    hours = (time%86400)/3600
    minutes = ((time%86400)%3600)/60
    seconds = (((time%86400)%3600)%60)%60
    
    days = math.trunc(days)
    hours = math.trunc(hours)
    minutes = math.trunc(minutes)
    seconds = math.trunc(seconds)
    
    print(str(days) + " days " +str(hours) + " hours " +str(minutes)+ " minutes " + str(seconds)+ " seconds")