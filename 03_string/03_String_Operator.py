'''String operators : 
    1. + : concarination 
        - We can only concate string with another string. 
        -  If we try to concate any other data type it will raise an error.
          Error : TypeError: can only concatenate str (not "int") to str

    2. * : repetation operator
        - We can only multiply with integer value no other data type.(boolean converted to true - 1 and false -0)
        - If we try to concate with float or string

    3. in , not in  : Membership operator
        - in → checks if a substring exists inside another string (or an element inside a list/tuple/dict).
        - not in → checks if a substring does not exist inside another string.
        - Always return a Boolean value (True or False). 
        - It is Case-sensitive and Works left-to-right

    4. < , <= , >, >=, ==,!= : Strong Comparision
        - This will compare string in Dictonary order. 
            Example : str = 'Abc' str2 = 'abcd' so string str comes before str2 so str < str2
        - These operators are used to compare two string values.
        - The result is always Boolean (True or False).
        - Special chars < Numbers < Uppercase < Lowercase
'''


str1 = "Hello "
str2 = str1+' world'
print(str2)



str2 = str1* 2
print(str2)
'''Give empty string'''
str2 = str1* False
print(str2)

str2 = 'Hello'
print(str2 in str1)

str2 = 'Helle'
print(str2 not in str1)


print("A" < "a")   # True → 65 < 97
print("Z" < "a")   # True → 90 < 97
print("9" < "A")   # True → 57 < 65
print("!" < "0")   # True → 33 < 48
print("@" < "A")   # True → 64 < 65

