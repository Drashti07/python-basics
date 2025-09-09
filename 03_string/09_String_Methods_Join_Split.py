'''

1. replace : this method will replace old string with the new string. 
            - if string present it will replace 
            - if ot present return original string

    signature : 
        string replace(old string , new String , count)
            where , - old string is the string that we want to replace
                    - new string is a string we want to replace with 
                    - count specify numbers of ccurance we want to replace, this is optional parameter


                    
2. join() : it insert string1 between all the character of string2
    signature : 
        str1.join(str2)
         - after each character of str2 the whole string str1 will ve appended.

3. split() : it will Splits a string into a list of substrings, using a specified separator

    signature :
        str.split(sep=None, maxsplit=all occurance)
            where : Parameters:
                - sep → separator string (optional).
                - If None (default), splits on any whitespace (spaces, tabs, newlines).
                - If separator given then it will remove that saparator and create list of substring.
                - maxsplit → optional, maximum number of splits (default -1, meaning unlimited).
           
3. rsplit() : it will Splits a string into a list of substrings from right , using a specified separator

    signature :
        str.split(sep=None, maxsplit=all occurance)
           

4. splitlines() : Splits a string at line boundaries (\n, \r, \r\n) and returns a list of lines.
        Signature :
            str.splitlines(keepends=False)
                    Parameters:
                    - keepends → optional (default False).
                    - If False, line break characters are removed.
                    - If True, line break characters are kept at the end of each line.
           
'''

str1 = 'drashti'

str2 = str1.replace('d','D')
print(str2)

str2 = str2.replace('i','i Patel')
print(str2)

str2 = str2.replace('d','D')
print(str2)

str3 = 'a-b-c-d-e-f'
print(str3.replace('-','/',2))


str1 = 'aaaaa'
str2 ='bbb'
print(str1.join(str2))


str1 = 'My is name is Drashti'
print(str1.split())
print(str1.split('is'))
print(str1.split('is',1))


s = "Hello\nWorld\r\nPython\rRocks"

print(s.splitlines())       
print(s.splitlines(True))   
print("NoNewLine".splitlines())  