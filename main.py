import random
import numpy as np
import matplotlib.pyplot as plp

List = [i for i in range(100,1000)]
onten = [i for i in range (1,10)]
zeten = [i for i in range (0,10)]
numb = random.choice(List)
print(numb)
first = round((numb - numb%100)/100)
second = round((numb%100 - numb%10)/10)
third = numb%10
numbl = np.array(first, second, third)
print(first, second, third)
print("Please, guess a three digit number.")
guess = int(input())
i = 0
while guess != numb or i == 10:
    while guess < 100 or guess > 999:
        print("This isn't three digit number. Please, guess THREE digit number")
        guess = int(input())
    i = i + 1
    guess1 = round((guess - guess % 100) / 100)
    guess2 = round((guess % 100 - guess % 10) / 10)
    guess3 = guess % 10
    print(guess1, guess2, guess3)
    guessl = np.array(guess1, guess2, guess3)
    res = numbl - guessl
    if np.product(res) == 0:
        print("Fico")
    elif


