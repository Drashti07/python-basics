'''split odd and even '''

List1 = [4,8,3,5,10,7,2,9,13,6]

odd = [x for x in List1 if x%2!=0]
even = [x for x in List1 if x%2==0]

print(List1)
print(odd)
print(even)



'''Pelindrom list '''

List3 = [5,4,3,3,4,5]
List4 =list(reversed(List3))
print(List3)
print(List4)

List4 = List3[::-1]
if List3 == List4:
    print("Pelindrom")
else:
    print("Not Pelindrom")


List4 = List3.copy()
List4.reverse()
if List3 == List4:
    print("Pelindrom")
else:
    print("Not Pelindrom")



'''Find Longest List'''

List1 = [[1,2,3],[1,1,1,1,1],[2,2,3,3]]
List2 = [ len(x) for x in List1]
print(List1)
print(List2)

print(max(List1 , key=len))


longest = 0
for x in List2:
    if x > longest :
        longest = x

print('lengrt is : ' ,longest)
