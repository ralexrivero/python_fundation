import random
import string

alpha = list(string.ascii_letters)
digits = list(string.digits)
special = list(string.printable[62:94])

print("Welcome to the password generator.")
user_a = int(input("How many letters would you like in your password?\n"))
user_d = int(input("How many numbers would you like?\n"))
user_s = int(input("How many symbols would you like?\n"))
password = []

for i in range(0, user_a):
    password.append(alpha[random.randint(0, len(alpha) - 1)])
for j in range(0, user_d):
    password.append(digits[random.randint(0, len(digits) - 1)])
for k in range(0, user_s):
    password.append(special[random.randint(0, len(special) - 1)])
random.shuffle(password)
for p in password:
    print(p, end='')
print()

password.clear()
