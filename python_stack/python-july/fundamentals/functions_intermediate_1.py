import random

def randInt(min=0, max=100):
    randNum = random.random()*(max)
    return(int(randNum))


print(randInt())
print(randInt(min=50, max=50))
print(randInt(min=50, max=100))
print(randInt(min=50, max=500))