''' In built string methods to change the cases of the string.
    1. captitalize() : Converts the first character of a string to uppercase and all other characters to lowercase.
    2. upper() : Converts all characters in a string to uppercase.
    3. lower() : Converts all characters in a string to lowercase.
    4. title() : Converts the first character of each word to uppercase and the rest to lowercase.
    5. swapcase() : Swaps the case of each character: uppercase → lowercase, lowercase → uppercase.
    6. casefold() : It is just like lower, convert all the latter to lower case but this can work with other 
                        languages too not only english, used for case-insensitive comparisons.

'''



str1= 'my name is Drashti Patel'

cap = str1.capitalize()
print(cap)

titl = str1.title()
print(titl)

upr = cap.upper()
print(upr)

lwr = upr.lower()
print(lwr)

casfld = upr.lower()
print(casfld)

swpcs = str1.swapcase()
print(swpcs)