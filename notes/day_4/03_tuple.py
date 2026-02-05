# Tuple is immutable 
# Tuple is used for storing important data since in tuple data cannot be change and it is safe..

a=(1,2,3,4,5)
print(type(a))
# output: <class 'tuple'>

b=(1)
print(type(b))
# output:  <class 'int'>        # this happens becz 1 is integer..

# To formed single value tuple we have to put one , only then it will become a tuple of single element
c=(2,)
print(type(c))
# ouput: <class 'tuple'>

# in tuple we can take any type of data string, integer , boolean etc....

z=(1,23.3,False,"anuj","shivam")
print(z) 
# output: (1, 23.3, False, 'anuj', 'shivam')

# if we want to change the any element of the tuple z we can't since tuple is a immutable