''' prefix and suffix methos : all this methods are case sensitive
    1. startswith() : it check if string starts with given prefix or not.
        signature : 
            boolean startswith(prefix , start, end)
                where start and end are optional and its default valie start = 0 and end = len(string)
                    - if start is < 0 then it automatically consider it to first index that is 0.
                    - if end is > len(str) then it automatically consider it to last index.
                    - empty string always gives true result
                    - tuple as prefix then it will return true if any one of it matches.

    2. endswith() : It checks if a string ends with the given suffix.
         signature :
            boolean endswith(suffix, start, end)
                where,  - suffix → string or tuple of strings to check
                        - start → optional, index to start checking (default = 0)
                        - end → optional, index to stop checking (default = len(string))3456890
                        - If start < 0, Python treats it as 0.
                        - If end > len(str), Python treats it as len(str).
                        - The check is done up to end-1 (exclusive).
                        - Empty string as suffix always returns True.
                        - Tuple as suffix → returns True if any element of the tuple matches.

    3. removeprefix() : Removes the specified prefix from the start of a string, if it exists.
                        If the string does not start with the prefix, it returns the original string unchanged.
                        Works with empty strings ("") safely — returns the same string.
    Signature:
        str.removeprefix(prefix)

    4. removesuffix() : Removes the specified suffix from the end of a string, if it exists.
                        If the string does not end with the suffix, it returns the original string unchanged.
                        Works with empty strings ("") safely — returns the same string.
    Signature:
        str.removesuffix(suffix)

    5. partition() : it partion string from first occurance the saparator from left.
        signature : 
            tuple partition(separator)
             - Splits the string into three parts: : (left_of_separator, separator, rigth_of_separator) 
             - If the separator is not found, it returns: (original_string, '', '')

    6. rpartition() : it partion string from first occurance the saparator from right.
        signature : 
            tuple partition(separator)
             - Splits the string into three parts: : (left_of_separator, separator, rigth_of_separator) 
             - If the separator is not found, it returns: ( '', '',original_string)

'''

str1 = "My Name is Drashti"

print(str1.startswith("My") )
print(str1.startswith('My' , 3))
print(str1.startswith('is' ,3 , 7))
print(str1.startswith('',-19,100))
print(str1.startswith(("My", "Hello")))  # tuple as prefix


print("endswith methos : ")
print(str1.endswith("shi") )
print(str1.endswith('Drashti' , 3))
print(str1.endswith('is' ,3 , 7))
print(str1.endswith('',-19,100))
print(str1.endswith(("My", "Hello" ,"Drashti")))  # tuple as prefix


str1 = 'AAriv'
print(str1.removeprefix('A'))
print(str1.removeprefix(''))
print(str1.removeprefix('B'))



str1 = 'ArivV'
print(str1.removesuffix('V'))
print(str1.removesuffix(''))
print(str1.removesuffix('A'))

str1 = "My Name Is Drashti"
print(str1.partition(" ")) #('My', ' ', 'Name Is Drashti')
#print(str1.partition(""))  empty separator not allow
print(str1.partition("Drashta"))

str1 = "My Name Is Drashti"
print(str1.rpartition(" ")) 
#print(str1.partition(""))  empty separator not allow
print(str1.rpartition("Mi"))