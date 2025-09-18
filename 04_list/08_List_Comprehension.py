'''
List Compehension : it will iterate over any iterabplr type daya type and ctrste a list

    syntext : [expression for item in iterable  if condition ]
        where , - expression → what you want to put in the new list
                - item → variable representing each element in the iterable
                - iterable → any sequence (list, tuple, range, string, etc.)


 Nested list : linst inside another list is called nested list 
        Example : List1 = [[1,2],[3,4]]
'''

tuple1 = (1,2,3,4,5)
LIST1 = list(tuple1)
print(LIST1)


List1 = [i*2 for i in tuple1 if i>2]
print(List1)

List1 = [[1,2],[3,4]]
print(List1[0])
print(List1[0][0])

