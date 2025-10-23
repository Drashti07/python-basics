'''
    what is function : Function is a piece of code that take some parameter perform an operation and return some value.
        - This functions are reusable

    Signature of function : 
        def function_name(<Parameters>):
                Statment 1
                Statment 2
                .
                .
                .
                Statment n
                return value
                
       ,  where def is a keywork
    how to call funtion :
        functionname(<value of parameters>)
    Arguments of function : there are 2 types of arguments 
            1. positional arguments : what ever argument we are passing
                all those argument inserted in order
                Example def volum(hight , length,width)
                        volum(10,5,5)
                        then hight: 10 , length : 5 , width : 5
                        
                        volum(5,10,5)
                        then hight: 5 , length : 10 , width : 5

            2. keyword arguments : 
                volum(width=5,hight =10,length=5)
                - in this if we change order value to that variable remain same
                - name must be same

            3. mixed argumet: we can also pass mixes argumets that is some positional 
                    and some keywords.
                    - rule :
                        - pass positional first then keyword
                        - if we try to assingn multiple value to same variable it will give error





def volumn(length , breth, hight):
    vol = length*breth*hight
    return vol

'''

'''if  __name__  =='__main__':
    """Calling function"""
    vol=volumn(10,5,3)
    print(vol)
'''

''' Default Argument : 

'''

def vol(l=1,b=1,h=1):
    v= l*b*h
    print(v)


vol()
vol(5)
vol(5,10)
vol(5,10,5)



def vol1(l=[1,2,3]):
    l.append(len(l))
    print(l)
  

vol1()
vol1(l=[10,11])
vol1(l=[10,11])
vol1()