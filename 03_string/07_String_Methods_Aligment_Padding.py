'''
1. ljust() : it left align string.
    - it will make the string length to width size and apen fillchar n right.
    - width < len(str)  then return exiting string
    signature :
        string ljust(width , fillchar=' ')
         where, filchar is optional and width is compalsory, defalut " ".
            - data type must be string only for fill character
            -fillchar len = 1 else raise an error
          
2. rjust() : it rigth align string.
    - it will make the string length to width size and apen fillchar n left.
    - width < len(str)  then return exiting string
    signature :
        string ljust(width , fillchar=' ')
         where, filchar is optional and width is compalsory, defalut " ".
            - data type must be string only for fill character
            -fillchar len = 1 else raise an error

3. center() : It aligh text in center and fill char on left and right.
            - if the width is not devided equaly then extra filling is done on left side.
         signature :
            str.center(width, fillchar=' ')
                where , -fillchar len = 1 else raise an error

4. Zfill() : Returns a new string of given width padded on the left with zeros
        Signature::
            str.zfill(width)

'''

str1 = 'Drashti'
str2= str1.ljust(1,'_')
print(str2 , len(str2))

str2= str1.ljust(10,'_')
print(str2 , len(str2))


str1 = 'Drashti'
str2= str1.rjust(1,'_')
print(str2 , len(str2))

str2= str1.rjust(10,'_')
print(str2 , len(str2))


str1 = 'Drashti'
str2= str1.center(1,'_')
print(str2 , len(str2))

str2= str1.center(10,'_')
print(str2 , len(str2))


a = '123.0'
str2 = a.zfill(7)
print(str2)


