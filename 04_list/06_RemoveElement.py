'''
REMOVE an Element from List 

1. remove() : it will remove first occurance of an element from the list.
        - if an element does not exist in the list it will raise an error

        signature : 
            list.remove(x)
        where, - x: the value to remove (first occurrence)
               - Return type: None (in-place)

 2. pop() : Removes the element at index i and returns it.
        - If index is not provided, removes last element.
        - Raises IndexError if list is empty or index out of range.
        signature : list.pop[i)

    where , - i: index of element to remove (optional, default = last element)\
            - Return type: the removed element              

 3.clear() : Removes all elements from a list.
    Signature: 
        list.clear()
    Return type: None

 4. del : it is in-place and does not return anything.
        - Great for bulk deletions or memory cleanup.
    Signature:
        del list : delete whole list. list it self so after this statment if you try to print list it will give you error.
        del list[i] : delete element at indec i
        del list[start , end] : delete all the element from start to end-1
'''

List1 = [1,1,2,3,4,5,6,7,1,8,2,3,1]
List2 = List1.remove(1)
print(List1)
print(List2)

print()
print()
List2 = List1.pop()
print(List1)
print(List2)
print()
print()
List2 = List1.pop(7)
print(List1)
print(List2)

print()
print()
#List2 = List1.pop(70)
#print(List1)
#print(List2)
print()
print()

List2 = List1.clear()
print(List1)
print(List2)


List2 = List1.clear()
print(List1)
print(List2)

List1 = [1,2,3,4,5,6,7,8,9]
del List1
#print(List1)
print()

List1 = [1,2,2,3,4,5,6,7,8,9]
del List1[2]
print(List1)
print()


List1 = [1,2,2,3,3,3,4,5,6,7,8,9]
del List1[2:5]
print(List1)