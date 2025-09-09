''' String Indexing : each elemt of stringa are store in an array internally so each characters are placed at a specific index.
                - Example : 'Hello'
                    1. positive index
                            index   Char
                              0      H
                              1      e
                              2      l
                              3      l
                              4      o

                    2. negative index
                             index   Char
                              -5     H
                              -4     e
                              -3     l
                              -2     l
                              -1     o
'''

str1 = 'Hello'
print(str1[0])
print(str1[-1])

'''
String Slicing : 
    - for slicing [] operator is used.
    - [strat : end : step]
        where   - strart : is starting index
                - ens is inding index (end-1)
                - step skip #of elelemt in between : Default value 1

'''

str2 = 'Hello World'
print('String length')
print(len(str2))
'''this represent index so it will just return element at the index 0
print(str2[0])'''

''' All 3 parametera are optiona; : print all the characters of the string  '''
print(str2[:])
print(str2[: :])

'''
    1. parameter : start 
        - default value of start :
            - if step is positive : start = 0 (beginning of string)
                -  positive start is given → slice runs from start to the end of string.
                - negative start is given → slice runs from start = (len(str)+start)to the end of string.
            - if step is negative : start = len(s) - 1 (end of string)
                - positive start is given → slice runs from start to the end = -1 (till first char of string and to include index 0 take -1) in reverse order.
                - negative start is given → Python converts it into start = len(str) + start, end = -1 ,then goes from start to the end(begining of string) and print in reverse order. 

        - When :
            -  step = +ve then start < end 
            - step = -ve then start > end
            - if this condition not satisfy then give empty string as a result
'''

str3 = 'Manish Patel'

print(str3[3:])
print(str3[-3:])
print(str3[-3::-1])
print(str3[3::-1])



''' 2. end parameter  :
        - default value of end : 
            - if step is positive : end = len(string)
                - positive end is given → slice runs from start to the end-1 of string.
                - negative end is given → Python converts it into end = len(str) + end,start = 0 then goes till that.
            - if step is negative : end =-1 i.e starting of string( we need index 0 so to include it take -1)
                - positive end is given → slice runs from start= len(str)-1i.e last chsr of string to the end-1 in reverse order.
                - negative end is given →  slice runs from start= len(str)-1 i.e last chsr of string to the end = len(str)-end in reverse order.
            
            - When :
                -  step = +ve then start < end 
                - step = -ve then start > end
                - if this condition not satisfy then give empty string as a result
'''  

str2 = 'Manish Patel'
print(str2[:5])
print(str2[:-5]) 
print(str2[:5:-1])
print(str2[:-5:-1])




'''only step then start from 0 and print every step element till end of string
in below case it wil print 0,2,4,6 index elements
    Rules to remember
        - Positive step → left to right (forward).
        - Negative step → right to left (backward).
        - If you leave start and end empty, Python picks defaults:
            - ::1 → start at 0, go to end.
            - ::-1 → start at last index, go to beginning.
 '''

print(str2[::2])
print(str2[::-1])



'''String are immutable : meaning if we try to change anything within the string it will not change existing string
                          insted it will creat a new string with those changes.

 below will give error
str2 = "Helle"
str2[-1] = 'o'

print(str2) '''


''' When we try to concate a string insted of adding content to same string it will create a new string with
concated content that is string immutability '''
str4 = "Helle"
str5 = str4 +' world'
print(str4)
print(str5)



