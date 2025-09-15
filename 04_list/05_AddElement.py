'''Mrthods to add elemets in to the list : 
        1. appen(elelemt) : Adds x as a single element at the end of the list. 
            Signature : 
                    None list.append(x) 
            where , Return type: None
                - Effect: Adds x as a single element at the end of the list.
                - Time complexity: O(1) average

        2. extend() : extend() is a list method in Python that adds all elements of an iterable to the end of the list, one by one.
            - It modifies the list in place and returns None.
            Signature :
                None list.extend(iterable) 
            Where, iterable: Any Python iterable (list, tuple, set, string, generator, dict, etc.).
                - if try to extend list with other then iterable data type gives an error.
                - Always return Always None.
            Internal Working

            Internally:
                - Python loops through the provided iterable.
                - Each element is appended to the end of the list using low-level operations.
                Internal code : 
                    def extend(lst, iterable):
                        for item in iterable:
                            lst.append(item)
        3. insert() : insert() inserts a single element of any type into a list at a specified index.
                - Unlike append() (always end) or extend() (bulk add at end), insert() lets you control the exact position.
            Signature : 
                list.insert(index, element)
            where , index: The position where the element should be inserted.
                    element: The object to insert.
                - The element is inserted before the given index.
                - If index = 0 or index < len(List)*-1, element is inserted at the start.
                - If index >= len(list), element is inserted at the end.
                - Shifts all elements from that index onward to the right.
        
         
        4. copy() : copy() creates a shallow copy of a list.
                That means:
                - A new list object is created.
                - It contains references to the same elements as the original (not deep copies)
            Signature : 
                new_list = list.copy()
                    - return list
    
'''

List1 = [1,2,3,4,5,6]
num = List1.append(7)
print(num)
print(List1)

num = List1.append('a')
print(num)
print(List1)

num = List1.append(1.9)
print(num)
print(List1)

num = List1.append([8,9])
print(num)
print(List1)

num = List1.append((10,11))
print(num)
print(List1)

num = List1.append({12,13})
print(num)
print(List1)

num = List1.append({'a':14,'b':15})
print(num)
print(List1)


print()
print('2. extend() method to add element in to the list')

List2 = [1,2,3,4]
num = List2.extend([5,6,7])
print(List2)
print(num)

num = List2.extend('Drashti')
print(List2)
print(num)

num = List2.extend((8,9,10))
print(List2)
print(num)

num = List2.extend({11,12,13,14})
print(List2)
print(num)

# this will just add keys not values
num = List2.extend({'a':1,'b':2,'c':3}) 
print(List2)
print(num)



print()
print('2. insert() method to add element in to the list')

List3 = [1,2,4,5,6,7,9]
num = List3.insert(2,3)
print(List3)

num = List3.insert(2,['a','b'])
print(List3)

num = List3.insert(-10,['insert at begining as index is < 0'])
print(List3)

List4 = [1,2,3,4,5]
List5 = List4.copy()
print(List5)