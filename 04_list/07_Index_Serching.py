''''
Other List index for searching and indexing

1. index: returns the index of the first occurrence of x.
        - Raises ValueError if not found.
    signature : 
        list.index(x, start, end)
    Where , - X is an element
            - start is an optional if not provided search from begining
            - end also optional, default = len(str)

2. count() : Scans the list from start to end.
            - Counts exact matches only (based on equality ==).
            - Case-sensitive for strings ("A" ≠ "a").
            - Works for numbers, strings, tuples, and other objects as long as they are comparable. 
    signature : 
        list.count(x)
    where , x: The element you want to count inside the list.
            - it return : int → the number of times x appears in the list. 
            - if value not present return 0.

3. reverse() : This function is used to perform in-place reversal.
    signature : 
        list.reverse()   
4. sort() : Sorts the list in place (changes the original list).
        - Returns None (not a new list).
        - Default: ascending order.
        - Optional:
            - reverse=True → descending order.
            - key=function → decide what Python looks at when sorting.
    signature : 
        list.sort(*, key=None, reverse=False) -> None
'''

'''S = int(input("how many values you want in list"))

List1 = []

for i in range(0,S):
    val = int(input("Enter value : "))
    List1.append(val)

print(List1)  
'''

List1 = [1,2,3,2,5,3,6,2]
indx = List1.index(2)
print(indx)

indx = List1.index(2,2)
print(indx)

indx = List1.index(2,4,10)
print(indx)


print()
print("count function :")
List2= [1,2,3,4,5,1,2,3,4,5,6,7,8,9,7,8,6,2]
print(List2.count(90))

List1 = [1,2,3,4,5]
List2 = List1.reverse()
print(List1)
print(List2)


List1 = [1,2,3,4,5,9,8,2,4,5,6,1,3]
List1.sort()
print(List1)

List1.sort(reverse=True )
print(List1)

words = ["banana", "apple", "cherry", "fig"]
words.sort(key=len)
print(words)