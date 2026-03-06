#Richter scale
magnitude = float(input("Enter the earthquake magnitude: "))

'''here we use the function [float] insted of [int]
float //accepts decimal and integer values like 5.6,3.5,..
whereas; int// only accepts integer values like name,8 ,..
'''

if magnitude < 2.0:
    descriptor = "Micro"
elif magnitude  < 3.0:
   descriptor = "Very minor"
elif magnitude  < 4.0:
   descriptor = "Minor"
elif magnitude  < 5.0:
    descriptor = "Light"
elif magnitude  < 6.0:
   descriptor = "Moderate"
elif magnitude  < 7.0:
   descriptor  = "Strong"
elif magnitude  < 8.0:
  descriptor  = "Major"
elif  magnitude  < 10.0:
  descriptor = "Great"
else:
  descriptor = "Meteoric"

''' here we use the function  [desciptor] to  track vairable values
  while coding or calculation '''

#f// is always the best option foe embedding variables with text 
# Display the meaningful message

print(f" magnitude{magnitude } earthquake is considered to be a {descriptor} earthquake.")