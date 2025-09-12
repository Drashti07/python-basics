'''List : List is the built in data type in python. 
      - Defination : A list in Python is an ordered, mutable, and heterogeneous collection of elements.
      - Ordered : Items maintain the sequence you insert them in.
        - We can access those element using index starting from 0.
      - Mutable : You can modify the list after creation (add, update, delete).
      - Hiteroginious : We can store all the type of elemts includeing another list , tuple , set , dictonary.
      - List can contain duplicate values. 
      - it is represented by []


     1. Create List : From Explicit valueq11     
        Syntext : 
            <Variable_Name> = [<ele1> , <ele2>, <ele3>,<ele4> ,.....]      
    
     2. list() : list constructor to create list from iterable objects (like strings, tuples, sets, ranges, etc.).
        Syntext : 
         <Variavle_name> = list(<Iterable>)
     3. list = [] : create an empty list and you can add elements later.

'''
print()
print()
print('create a list from explicit values')
List1 = [1,2,3,4,5]
print(List1)

# o/p : [1, 2, 3, 4, 5] 
print()
print('List is Heterogenious : can contain all the type of elements')
List2 = [1, 2.0 ,'Drashti', [1,2,3],(4,5),{5,6},{'name': 'Drashti', 'age': 25}]
print(List2)

print()
print('type() constructor to convert string to List')
S = "Drashti"
List1 = list(S)
print(List1)

print()
print('type() constructor to convert tuple to List')
S = (1,2,3,4,5)
List1 = list(S)
print(List1)

print()
print('type() constructor to convert set to List')
S = {1,2,3,4,5}
List1 = list(S)
print(List1)

# For dictonary this function create list of keys only.
# Create list of values and both key-values pair will be covered under dictonary 

print()
print('type() constructor to convert dictonary to List : It will create Keys of list')
S = {'1':'a','2':'b','3':'c','4':'d','5':'e'}
List1 = list(S)
print(List1)



''' 2. Accessing element of list :
        1. Using Index : List store elelemts in order, so we can access elelemt using index. 
                         - index start from 0.

        2. From beging : use positive index to iterate over list from begining: 
                for (<var> in range(0,len(list),1)) 
                    or
                for var in <list_name> : 

        3. from End : use negative index to iterate over list from end.
                for (<var> in range(-1,len(List)*-1,-1))
                - -1 means last elemet of the list 
                - -2 second last .....

    - To check type of elelemt typr(<elelemt>) function is used.
    Note :- List store referance of the element, not the actual element.
'''
print()
print('Access element using Index')
List1 = [1,2,3,'d','e',6]
print(List1[0])
print(List1[2])
print(List1[4])
print()

print('check type of element')
print(type(List1[0])) # <class 'int'> int class means int type of elemet 
print()

print('Access Elements of List')
# from begining :
for i in range(0,len(List1),1):
    print(List1[i] , end = ' ' )
print()

# from begining 

for i in List1:
    print(i , end = ' ')
print()

#from End :
for i in range(-1,(len(List1)+1)*-1,-1):
    print(List1[i] , end = ' ' )
print()



'''Length of List : to find how many numbers of elements a list has.
    syntext : 
        int len(<List_Name >)'''


List1 = [1,2,3,4]
print('length of List : ' , len(List1))

List1 = []
print('length of empty List : ' ,len(List1))


