# Mērķis: 
# uzģenerēt paroli no burtiem un cipariem noteiktā garumā

import random
import string


password_length = int(input("Kāds būs garums?"))

password = ""
for i in range(password_length):
    if i % 2 == 0:
        password += str(random.randint(0, 9))
    else:
        password += random.choice(string.ascii_letters)

print("Jauna parole:", password)

# Kādas kļūdas izdevies atrast?
# missing spaces when inside 'for', 'if' and 'else'
# else is missing ':' after it
# misspelled variable name 'password'
# library 'random' now imported
# misspelled 'random'
# varieble 'password_length' unused, its supposed to be the length of 'for' cycle

