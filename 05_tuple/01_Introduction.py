''' tuple : Tuple is created using (). 
        - It also store elelemt in the order it is inserted meaning it preserve insertion order.
        - it allow duplicate.
        - it is also hitroginious like list.
        - but it is immutable means once it is created it can not be changed (i.e can not modify , delete,add elelemt in it).

'''

'''Creating tuple

        1. <variable name> = (<element1>,<element2>,<element3>.....) 
            Where () brecket are optional 
        2. <variable name> = tuple(<iterator>) 
            where iterator can be string , list , set , dictonary
'''

Tuple1 = (1,2,3,4,5,6)
Tuple2 = (1.1,2.2,3.3)

# Allow duplicate insertion 
Tuple1 = (1,2,3,4,5,6,1,2,3)
print(Tuple1)

# tuple is hitroginious
Tuple3 = (1 , 'a',1.1,True,[1,2])
print(Tuple3)

#create empty tuple
Tuple5 = ()

#convert iterable to tuple using tuple() method - it just take iterable not integer that is 
# tuple(3,) will give error
Tuple4 = tuple("Drashti")
print(Tuple4)

Tuple4 = tuple([1,2,3,4])
print(Tuple4)

Tuple4 = tuple({1,2,3,4})
print(Tuple4)

Tuple4 = tuple({'a':1 , 'b':2,'c':3})
print(Tuple4)

#create tuple for single vartiable must use , at end

Tuple6 = (3,)
print(Tuple6)

# By degalt in python if multiple values are assign to one variable it will create a tuple

Tuple7 = 1,2,3,4,5,6
print(Tuple7)

'''
# Tuple is immutable meaning once cerated can not be modify
# It gives an error TypeError: 'tuple' object does not support item assignment
Tuple8 = (1,2,3,4,5,6,7)
Tuple8[0]=10
print(Tuple8)'''

#Traversal 
''' 1. using for loop'''
for i in Tuple7:
    print(i , end = " ")
print()

'''2. using range'''
for i in range(0,len(Tuple7)):
    print(Tuple7[i], end = " ")
print()

'''3. in reverse order using negative index'''


for i in range(-1,(len(Tuple7)*-1)-1 , -1):
    print(Tuple7[i], end = " ")
print()