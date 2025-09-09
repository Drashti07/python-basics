''' 
1. find() : It give the index of the strings first character from the left.
            - if string present it return index 
            - if string not present it will return -1
    signature : 
        int find(string , start , end)
        where , - start and end are optional and default start = 0 , end = len(str)
            - start must be within valid range only else it will give -1 even if the string is present.
            - end > len(str) it will mapped to len(str)
            - Works with empty substring: str.find("") always returns start.

2. rfind() : it is same as finf but it find a string from right side. 
    signature : 
        int rfind(substring, start=0, end=len(str))
Note : - ind() returns the first occurrence from the left.
       - rfind() returns the last occurrence from the right.

3. index() : It is similar to find from left but if the string is not present then it throw an error.
    signature :
        int index(substring, start=0, end=len(str))

        - empty string - return 0

4. rindex() :  It is similar to find from left but if the string is not present then it throw an error.
    signature :
        int rindex(substring, start=0, end=len(str))

         - empty string - return len(str)

5. coubnt() : it give string is how many time occurs in the string
            - If substring is not found, returns 0
    signature : 
        int count(substring, start=0, end=len(str))

        where - start and end are optional; default: start=0, end=len(str).
                - Counts only non-overlapping occurrences.
                - Search is performed from left to right.
                - Works with empty substring: returns len(str) + 1 (every position between characters counts as an occurrence).

'''

str1 = 'Hi, How are you'
print(str1.find('How'))
print(str1.find('Hi' , -2))
print(str1.find('is',90))
print(str1.find('How', 0 , 90))

print()
str1 = 'Hi, How are you'
print(str1.index('H'))
print(str1.index('')) # 0 


str1 = 'Hi, How are you'
print(str1.rindex('H'))
print(str1.rindex('')) # len(str) last index


print(str1.count('H'))
print(str1.count(''))
print(str1.count('h'))