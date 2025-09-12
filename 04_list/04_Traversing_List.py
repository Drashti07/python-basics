'''
Traversing List : iteration over each elelemt of the List.
        1. for loop
        2. for loop with rang() function
        3. while loop
        
'''
print()
print('for loop :')
List1 = [1,2,3,4,5,6,7]
for i in List1 :
    print(i)

print()
print('for loop with range:')
for i in range(0,len(List1),1):
    print(List1[i])


print()
print('while loop :')
i = 0
while i<len(List1):
    print(List1[i])
    i = i+1