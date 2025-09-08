'''
String : string is nothing but sequence of character written in either '' or "".
        - string is immutable in python so once we create it we can not modify existing string.

How to create a string in python : 
        we can create a string by s = '<anything>' or s ="<Anything>"

to represent'' or "" inside a string s = 'Drashti"s' or s = "Drashti's"        
'''

str1 ='String representation'
print(str1)

str2 = "string representation"
print(str2)

str7 = "Drashti's"
print(str7)


str8 = 'Drashti"s'
print(str8)

'''
String representaion in memory : In memory string is representated in the form of
        an array. 
        Example : "Hello"
                H will be at index 0 , e at 1 ,l at 2 , l at 3 and o at 4
                this index starts form 0
        - it support +ve and -ve both indexing :
                - positive index is to traverse string from begining and it starts from 0.
                        - Ex : Hello : 0 for H , 1 for e , 2 for l , 3 for l , 4 for o
                - negative index is to travers string from end(reverse order) and it starts from -1.
                        - EX: Hello : -1 for 0 , -2 for l , -3 , for l , -4 for e , -5 fpr H
'''


str3 = 'String Indexing'
print(str3[0]) 
print(str3[-1])
print()

''' Reverse a string usin -ve index '''
for i in range(1,len(str3)+1):
    print(str3[-1*i], end=' ')
print()



'''Length of string : Length of string means the total numbers of charater present in the string
        - Example : 'Hello' its length is 5 , for empty string'' length is 0
        - to find a length of string len() function is used 
        Signature : int len(<String>)
 '''


str4 = "Lenght of string"
print(len(str4))

str5=''
print(len(str5))


'''Traversing a string : means visiting each element of the list 
        - string can traverse using for loop :
                -  each charater 
                - based on index
        Example : in below for loop i is first at H once it printed 
                - then move to e print e
                - then move to l print l
                - then move to l print l
                - then move to o print o
                once it reach at end of list it stop loop.
'''
EachCaracter="String Traversal each character"
for i in EachCaracter:
    print(i)

print()

UsingIndex = 'traversing using index'

for i in range(len(UsingIndex)):
    print(UsingIndex[i] , end = ' ')










