'''String operators : 
    1. + : concarination 
        - We can only concate string with another string. 
          If we try to concate any other data type it will raise an error.
          Error : TypeError: can only concatenate str (not "int") to str

    2. * : repetation operator
        - We can only multiply with integer value no other data type.(boolean converted to true - 1 and false -0)
        If we try to concate with float or string
    3. IN , NOT IN  : Membership operator
    4. < , <= , >, >=, ==,!= : Strong Comparision
'''


str1 = "Hello "
str2 = str1+' world'
print(str2)



str2 = str1* 2
print(str2)
'''Give empty string'''
str2 = str1* False
print(str2)

