'''Slicing : 
    Syntext : 
        list_name[start : end  : step ]
            - where,
                - start : index to begin slice (inclusive). Defaults to 0.
                - end : index to stop slice (exclusive). Defaults to len(list).
                - step : interval (stride). Defaults to 1.

'''
print()
print()
print("Slicing to Read list")
# all three parameter optional if nothing given it will give whole list
List1 = [1,2,3,4,5,6,7,8,9]

#print(List1[::]) invalid syntext
print(List1[:])
print(List1[::])

# only start given
print('only start parameter given ')
print(List1[2:])
print(List1[-2:]) # this is similar to print(List1[-2::1])
 # default step = 1 and end = len(list) 
#   when step 1 : then read list from begining to end
#   when step -1 : then read list in reverse or from  end to begining 
# in above example start = len(lst)+-2 , end = len(list) , strp = 1 means [7:9:1]

print(List1[-2::-1]) # [7:-1:-1] for -ve step end default is -1 and start len(list)+start
print(List1[2::-1])

print()
print()
print('only end parameter given ')
print(List1[:4])
print(List1[:-4])

print(List1[:4:-1])
print(List1[:-4:-1])


print()
print()
print('all parameter')
'''
    - step is +ve : start < end
    - step -ve star > end
    - if this condition not satisfy then give empty string as a result
'''

print(List1[2:6:1])
print(List1[-4:-6:-1])

print(List1[2:6:-1])
print(List1[-4:-6:1])



'''String is mutable so we can perform read and write both on it 

        using index : 
            List[<index>] = <new_value>
                where index can be +ve or -ve
                 - this value can be anything string , numeric type , tuple , list , set or dictonary
'''
print()
print('Write on index ')
List1 = [1,2,3,'d',5,6]
print('List before modifing : ' , List1)
List1[3] = 4
print('List after modifing : ' , List1)
List1[3] = ['A','B']
print('List after modifing : ' , List1)

# if index is > len(List) then give an IndexError: list assignment index out of range
#List1[6] = 4 
#print('gives an error as index is > len(List1) : ' , List1)


'''
    writting using Slicing : replaces all elements from index start up to (but not including) end with the elements in new_list.
                    - If the slice is non-empty, it replaces those elements.
                    - If the slice is empty, it inserts the new elements at the position of start.
       
        Syntext : 
            list[start:stop:step= 1] = [< any numbers of new elelemts>]

            list[start:stop:step > 1] = [<Exect numbers of new elelemts>]
                    where, 
                        - if step = 1  then length of new elelemts can be anything i.e if start and stop replacing just 2 element and new elelemts are 4
                        its fine we can replace it.  
                        - if step > 1 is given then must have to give exect numbers of value               
            
'''
print()
print('Write using slicing ')
List1 = ['A','B',"C","D",1,2,3,4,5,6,7]
print(List1)
List1[0:4] = [11,22,[33,44]]
print(List1)

List1 = ['A','B',"C","D",1,2,3,4,5,6,7]
List1[10:3] = [11,22,[33,44]]
print(List1)

# slicing return [] empty list so it will not replace any value in existing list but it insert value at starting 
# index and move all the other elelemt 

List1 = ['A','B',"C","D",1,2,3,4,5,6,7]
List1[-1:-3] = [11,22,[33,44]]
print(List1)


# slicing return [] empty list so it will not replace any value in existing list but it insert value at starting 
# index and move all the other elelemt 

List1 = ['A','B',"C","D",1,2,3,4,5,6,7]
List1[3:1] = [11,22,33,44]
print(List1)

List1 = ['A','B',"C","D",1,2,3,4,5,6,7]
List1[0:4:2] = [11,22]
print(List1)

#step > 1 so must have exect numbers of 
#List1[0:4:2] = [11,22,33]
#print(List1)

