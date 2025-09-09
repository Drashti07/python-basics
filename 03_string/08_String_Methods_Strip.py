''' Strip methos : 
1. lstrip() : Removes leading characters (from the left) from the string.
            - By default, removes whitespace.
            
        Signature:
            str.lstrip(chars=None)
            where , chars is optional. If provided, removes all characters in the chars string from the start.

2. rstrip() :Removes leading characters (from the right) from the string.
            - By default, removes whitespace.
            
        Signature:
            str.rstrip(chars=None)
            where , chars is optional. If provided, removes all characters in the chars string from the start.

3. strip() : Removes both leading and trailing characters.
            - By default, removes whitespace.
        Signature:
            str.strip(chars=None)

'''

str1 = 'aaaa This is string '
print(str1.lstrip('a'))

str1 = '  This is string'
print(str1.lstrip())


str1 = 'This is string aaaa'
print(str1.rstrip('a'))

str1 = 'This is string.  '
print(str1.rstrip())


str1 = '  This is string.  '
print(str1.strip())