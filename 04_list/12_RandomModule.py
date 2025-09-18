'''Random module : 
1. random() : it generate rando numbers from 0 and 1 
2. randint(start , end) : it generate random number between start and end
3. randrange(start, stop, step) : Random number from range (like range())
5.random.choice(seq) : Pick one element
5. random.choices(seq, k=n) : Pick n random element with replacement
6.random.sample(seq, k=n) : Pick n unique elements (no replacement)
7.random.shuffle(seq) : to shuffle in place 
8.random.seed(<num>) : each time it will generate same number 

'''
import random as rd

print(rd.random())

print(rd.randint(1,100))
print(rd.randrange(1,10,2))

List2 = [4,5,6,7,8]
print(rd.choice(List2))
print(rd.choices(List2 , k=5))
print(rd.sample(List2,k=3))

List2 = [4,5,6,7,8]
print(rd.shuffle(List2))
print(List2)
List2 = [4,5,6,7,8]
rd.seed(100)
print(rd.choices(List2 , k=4))