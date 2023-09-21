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
numbl = np.array([first, second, third])
print(first, second, third)
print("Please, guess a three digit number.")
guess = int(input())
i = 1
while guess != numb or i == 10:
    while guess < 100 or guess > 999:
        print("This isn't three digit number. Please, guess THREE digit number")
        guess = int(input())
    print("Guess", i)
    i = i + 1
    guess1 = round((guess - guess % 100) / 100)
    guess2 = round((guess % 100 - guess % 10) / 10)
    guess3 = guess % 10
    print(guess1, guess2, guess3)
    guessl = np.array([guess1, guess2, guess3])
    res = [i for i in guessl-numbl if i == 0]
    pico = [i for i in guessl if i in numbl]
    if len(res) == 1:
        print("Fermi")
    elif len(res) == 2:
        print("Fermi, Fermi")
    elif len(pico) == 1:
        print("Pico")
    elif len(pico) == 2:
        print("Pico, Pico")
    else:
        print("Bagels")
    guess = int(input())
if guess == numb:
    print("Congratulations, you won!")
else:
    print("You lost :(")


