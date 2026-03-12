#python challenges
# Generate a random number integer between one and hundred and check if the result is an even number
import random
print(random.randint(1,100))

number = random.randint(1,100)
if number % 2 == 0:
    print(f"{number} is a even number")
else:
    print('not a even number')