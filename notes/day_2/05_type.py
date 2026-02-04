# Demonstrating the use of type() function to check variable types

# Integer variable
a=31
t=type(a) #class <int>
print(t)

# Float variable
b=3.14
t2=type(b) #class <float>
print(t2)

# String variable
name = "Alice"
t3=type(name) #class <str>
print(t3)

# Boolean variable
student = True
t4=type(student) #class <bool>
print(t4)

# NoneType variable
e= None
t5=type(e) #class <NoneType>
print(t5)

# Demonstrating type conversion in Python

# Converting integer to float
int_var = 10
float_var = float(int_var)  # converts to 10.0
print("Integer to Float:", float_var)

# Converting string to integer
str_var = "123"
int_var2 = int(str_var)  # converts to 123
print("String to Integer:", int_var2)

#converting integer to string
int_var3 = 456
str_var2 = str(int_var3)  # converts to "456"
print("Integer to String:", str_var2)
