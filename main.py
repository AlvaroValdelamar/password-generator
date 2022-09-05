import random
import string

length = int(input('Password length: '))

lowercase_letters = string.ascii_lowercase # [a,z]
uppercase_letters = string.ascii_uppercase # [A,Z]
numbers = string.digits # [0,9]
special_characters = string.punctuation #  !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~ 

all_characters = lowercase_letters + uppercase_letters + numbers + special_characters 


password = random.sample(all_characters, length)
password = "".join(password)
print('Your password is:\n')
print(password)