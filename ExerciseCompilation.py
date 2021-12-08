"""This is a compilation of the exercises I've done to practice python code.
   Feel free to explore beginner coding

   Attempts
"""




def miles_to_feet(x):
    feet = 5280
    ratio = x * feet
    print(ratio)
    return(ratio)

miles_to_feet(10)

def total_seconds(hours,minutes,seconds):
    return(hours * 60 + minutes) * 60 + seconds

hours, minutes, seconds = 7, 21, 37
print(str(hours) + " hours, " + str(minutes) + " minutes, and " + str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + " seconds.")

def rectangle_perimeter(width, height):
    x = (2*(width + height))
    return(x)

width, height = 5, 2
print("The rectangle perimeter is: " + str(rectangle_perimeter(width, height)))

def rectangle_area(width, length):
    x = width * length
    return(x)

width, length = 5, 2
print("The rectangle area is: " + str(rectangle_area(5,2)))

def circle_circumference(radius):
    pi = 3.141592
    multiplier = 2
    x = multiplier * pi * radius
    return(x)

radius = 1
print("The circumference of a circle is: " + str(circle_circumference(radius)))

def future_value(present_value,annual_rate,years):
    interest = 0.01
    present_value = (annual_rate * interest) ** years
    return(present_value)

present_value = 10
annual_rate = 2
years = 5
print("The current value is: " + str(present_value) + " " + "The annual rate is: " + str(annual_rate) + " " + "It will be compounded to: " + str(future_value(present_value, annual_rate, years)))


