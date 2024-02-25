import random


randZeroToOne = random.random()
print(randZeroToOne)

randRangeFloat = random.uniform(1,50)
print(randRangeFloat)

randInt = random.randint(1, 20)
print(randInt)

randRange = random.randrange(1, 20)
print(randRange)

list = [1,34,67,89,12, 'hello', 'world', 'python']
list2 = range(0, 50)
randChoice1 = random.choice(list)
randChoice2 = random.choice(list2)
print(randChoice1)
print(randChoice2)

randSample = random.sample(list, 3)
print(randSample)

