import random
a = [random.randint(0, 100) for _ in range(random.randint(20, 50))]
b = [random.randint(0, 100) for _ in range(random.randint(20, 50))]
print([x for x in b if x in a and a.count(x) == 1 and b.count(x) == 1])
