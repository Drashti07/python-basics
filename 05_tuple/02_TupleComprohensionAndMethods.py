'''
Tuple comprehension : It will itrate over each elelemt of the iterator and create a tuple

    Syntext = (*(<expresion> for x in itertator if <Condition>),)


'''
# this will not give tuple it willl give generator object
t = (x*x for x in range(5))
print(t)

t = (*(x*x for x in range(5)),)
print(t)