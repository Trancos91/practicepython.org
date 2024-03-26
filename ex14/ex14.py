#!/usr/bin/env python3
import random
def create_random_list(n):
    random_list = []
    for x in range(n):
        x = random.randint(0, 100)
        random_list.append(x)
    return random_list
def delete_duplicates_comp(old_list):
    new_list = []
    for x in old_list:
        if new_list.count(x) == 0:
            new_list.append(x)
    return new_list
def delete_duplicates_set(old_list):
    new_set = set(old_list)
    return new_set
random_list = create_random_list(int(input("Ingresá el largo de a lista que querés armar en números: ")))
print("La lista que se generó es:")
print(random_list)
print("La lista sin duplicados usando list comprehension es:")
print(delete_duplicates_comp(random_list))
print("La lista sin duplicados usando sets es:")
print(delete_duplicates_set(random_list))
