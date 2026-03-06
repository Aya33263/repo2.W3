#sound level

# Get the sound level from the user

db = float(input("Enter the sound level in decibels (dB): "))

# Check for exact matches or range using if,elif,<,>,=

if db > 130:
    print("This is louder than a jackhammer.")
elif db == 130:
    print("Jackhammer")
elif 106 < db < 130:
    print("The sound is between a petrol lawnmower and a jackhammer.")
elif db == 106:
    print("Petrol lawnmower")
elif 70 < db < 106:
    print("The sound is between an alarm clock and a petrol lawnmower.")
elif db == 70:
    print("Alarm clock")
elif 40 < db < 70:
    print("The sound is between a quiet room and an alarm clock.")
elif db == 40:
    print("Quiet room")
else:
    print("This is quieter than a quiet room.")

    # we check db alone and between  two values 