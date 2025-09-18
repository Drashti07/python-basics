'''Remove duplicate from a list '''

List1 = [3,5,7,9,3,6,5,2,3,7]
List2=[]
for x in List1 :
    if List2.count(x) ==0 :
        List2.append(x)

print(List1)
print(List2)


List1 = [3,5,7,9,3,6,5,2,3,7]
List2=[]
for x in List1 :
    if x not in List2 :
        List2.append(x)

print(List1)
print(List2)