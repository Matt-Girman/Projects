"""
Matthew Girman

Distance Traveled
10/9/19
"""

initial_speed = int(input("Enter the speed of the vehicle in mph: "))
hours = int(input("Enter the number of hours traveled: "))

print("Hour     Distance Traveled")
print("--------------------------")

x = 0
speed = initial_speed

while x < hours:
    print(str(x+1) + "         " +str(speed))
    
    x += 1
    speed += initial_speed