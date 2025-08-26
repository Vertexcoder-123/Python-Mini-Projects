import string
import random

symbols = list(string.ascii_letters)

card1 = [0]*5
card2 = [0]*5

pos1 = random.randint(0,4)
pos2 = random.randint(0,4)
while pos2 == pos1:  
    pos2 = random.randint(0,4)

samesymbol = random.choice(symbols)
symbols.remove(samesymbol)

card1[pos1] = samesymbol
card2[pos2] = samesymbol

i = 0
while i < 5:
    if i != pos1:
        alphabet1 = random.choice(symbols)
        symbols.remove(alphabet1)
        card1[i] = alphabet1
    i += 1

i = 0
while i < 5:
    if i != pos2:
        alphabet2 = random.choice(symbols)
        symbols.remove(alphabet2)
        card2[i] = alphabet2
    i += 1

print("Card 1:", card1)
print("Card 2:", card2)

ch = input("Spot the similar symbol: ")
if ch == samesymbol:
    print("Right")
else:
    print("Wrong! It was:", samesymbol)
