import random
import numpy as np

List = [i for i in range(100,1000)]
onten = [i for i in range (1,10)]
zeten = [i for i in range (0,10)]
numb = random.choice(List)
#print(numb)
first = round((numb - numb % 100)/100)
second = round((numb % 100 - numb % 10)/10)
third = numb % 10
numbl = np.array([first, second, third])
j = 1
#print(first, second, third)
print("Please, guess a three digit number.")
guess = int(input())

while guess != numb and j < 10:
    while guess < 100 or guess > 999:
        print("This isn't three digit number. Please, guess THREE digit number")
        guess = int(input())
    print("Guess", j)
    j = j+1
    guess1 = round((guess - guess % 100) / 100)
    guess2 = round((guess % 100 - guess % 10) / 10)
    guess3 = guess % 10
    #print(guess1, guess2, guess3)
    guessl = np.array([guess1, guess2, guess3])
    res = [i for i in guessl-numbl if i == 0]
    res1 = ['0', '0', '0']
    for i in range(0, 3):
        if guessl[i] == numbl[i]:
            res1[i] = guessl[i]
    #print(res1)
    pico = [i for i in guessl if i in numbl]
    pico = list(pico)
    a = len(res)
    pico1 = [i for i in pico if i not in res1]
    #print(pico1)
    b = len(pico1)
    if len(res) == 2:
        print("Fermi "*a)
    elif len(pico) != 0:
        print("Fermi "*a, "Pico "*b)
    else:
        print("Bagels")
    guess = int(input())
if guess == numb:
    print("Congratulations, you won!")
else:
    print("You lost :(")


