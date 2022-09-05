import random
import string

#------------------------------------
# USER INPUTS
#------------------------------------

# Password length input by user
length = int(input('Password length: '))

# Password should have uppercase letters, yes or no
uppercases = input('Password should have upper cases? y/n: ')
assert uppercases == 'y' or uppercases == 'n', "Answer should be 'y' or 'n'"

# Password should have numbers, yes or no
nums = input('Password should have numbers? y/n: ')
assert nums == 'y' or nums == 'n', "Answer should be 'y' or 'n'"

# Password should have special characters, yes or no
special_chars = input('Password should have special characters? y/n: ')
assert special_chars == 'y' or special_chars == 'n', "Answer should be 'y' or 'n'"


#------------------------------------
# CHARACTERS IN PASSWORD GIVEN INPUTS
#------------------------------------
# Now the characters that should be on the password are:

lowercase_letters = string.ascii_lowercase # [a,z]

if uppercases == 'y' :
    uppercase_letters = string.ascii_uppercase # [A,Z]
else:
    uppercase_letters = ''

if nums == 'y' :
    numbers = string.digits # [0,9]
else:
    numbers = ''

if uppercases == 'y' :
    special_characters = string.punctuation #  !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~ 
else:
    special_characters = ''

all_characters = lowercase_letters + uppercase_letters + numbers + special_characters 


#------------------------------------
# PASSWORD GENERATOR
#------------------------------------
# We take a sample from the pool of all of the posibles characters given the password length 
password = random.sample(all_characters, length)
password = "".join(password)
print('Your password is:\n')
print(password)