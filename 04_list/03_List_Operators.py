'''' Operations on List :
    Operations apply on List are : 
    1. + : Concate 2 List
        - Concate only list with another list no any other data type
    2. * : reperation of list
    3. IN , NOT IN : member ship operation to check its in list or not
    4. < , <= , >, >= , == , != : to compare 2 list 
'''

'''Concanate List : 
    1. + operator : It will concate two List and result store in a new list 
        List1 + List2 + ..... + Listn
    2. extend() function : It will concate second list in to the first list. it willl not crear a new list
            List1.extend(List2)
                - Can take concare 2 list at a time 
                - can not chain(perform nesting of this fuction)

'''
List1 = [1,2,3,4]
List2=[5,6,7]
List3=[8,9,10]
print(List1+List2+List3)

List1 = [1,2,3,4]
List2=[]
print(List1+List2)

# Error : can only concatenate list (not "int") to list
#List1 = [1,2,3,4]
#print(List1+5)

List1 = [1,2,3,4]
List2 = [5,6,7,8]
List3=[8,9,10]
# List1.extend(List2.extend(List3))  TypeError: 'NoneType' object is not iterable
List2.extend(List3)
List1.extend(List2)
print(List1)
print(List2)


'''2. Repetation of string : * is used for it  
        Syntext : 
            List*<Integer> 
            where it only accept integer number no other then that.
        - It store result in a new list do not midify the existing list

'''

List1 = [1,2,3]
List2 = List1*3
print(List1)
print(List2)


'''
3. IN , Not IN : membership function 
    It is used to check if the elelemt is present in List or not 
    
    Signature : boolean X IN/NOT IN <List>

    -When we call in , not in , Internally it will call equal() method and start scanning elements from left to end of the list if value 
      present in list return True and stop traversing else return False.
'''

List1 = [1,2,3,4,5,6,7,8,9]
print(5 in List1)
print(5 not in List1)



'''
4. < , <= , > ,>= ,== , != : This list comparision function check each index elelemt and then give result if 
    it < , <= , > , >= , == , !=
'''

List1 = [1,2,3]
List2 = [1,4,3]
print(List2<=List1)
print(List2>=List1)

List1 = [1,2,3,4]
List2 = [1,2,3]
print(List2==List1)
print(List2!=List1)
print(List2<=List1)
print(List2>=List1)
