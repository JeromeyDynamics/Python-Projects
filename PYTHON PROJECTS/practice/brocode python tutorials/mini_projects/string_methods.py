# -------------------------------
# STRING METHODS
# -------------------------------
# name = input("Enter your name: ")
# phone_number = input("Enter your phone #: ")

# length = len(name) #returns length of word
# index = name.find(" ") #returns the first occurance of the thing in the find function
# name = name.capitalize() #returns a string where the first character is upper case and the rest are lower case
# name = name.upper() #returns the string upper case
# name = name.lower() #returns the string lower case
# result = name.isdigit() #returns true if all of the characters are digits
# result = name.isalpha() #returns true is all of the characters are alphabet letters
# result = phone_number.count(" ") #returns the number of elements with the specific value
# phone_number = phone_number.replace("-", "") #replaces all occurances of a specific phrase with the second 

# -------------------------------
#        EXERCISE
# -------------------------------
username = input("Enter a username: ")

if len(username) > 12:
   print("Your name can't be more than 12 characters")
elif not username.find(" ") == -1:
   print("Your username can't contain spaces")
elif not username.isalpha():
   print("Your username can't contain digits")
else:
   print(f"Welcome {username}!")