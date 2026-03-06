#Chinese Zodiac
#Get the year from the user
year = int(input("Enter a year: "))

#find the position in the 12-year cycle
remainder = year % 12

# Match the remainder to the animal
if remainder == 8:
    animal = "Dragon"
elif remainder == 9:
    animal = "Snake"
elif remainder == 10:
    animal = "Horse"
elif remainder == 11:
    animal = "Sheep"
elif remainder == 0:
    animal = "Monkey"
elif remainder == 1:
    animal = "Rooster"
elif remainder == 2:
    animal = "Dog"
elif remainder == 3:
    animal = "Pig"
elif remainder == 4:
    animal = "Rat"
elif remainder == 5:
    animal = "Ox"
elif remainder == 6:
    animal = "Tiger"
else:
    animal = "Hare"

print(f"{year} is the year of the {animal}.")