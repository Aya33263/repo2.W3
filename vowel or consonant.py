#vowel or consonant
# Get input and convert to lowercase for consistency use lower()

letter=input ("Please enter a letter of the alphabet: ").lower()

# Check if the letter is in the list of vowels

if letter in ('a', 'e', 'i', 'o', 'u'):
    print(f"The letter '{letter}' is a vowel.")

# Check the special case for 'y'
elif letter == 'y':
    print("Sometimes 'y' is a vowel, and sometimes it's a consonant.")

#If it's not a vowel and not 'y', it must be a consonant
else:
    print(f"The letter '{letter}' is a consonant.")

   # By using .lower(), we handle cases where a user 
   # might type "E" or "A". Without it, the program
   #  might skip the vowel check and incorrectly call "E" a consonant
   #  because "E" does not equal "e".