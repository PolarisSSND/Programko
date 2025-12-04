from random import randint
from graf import graf 
hodnoty = []
for u in range (100):
    hodnoty.append(randint(1,20))
hodnoty.sort()
graf(hodnoty)