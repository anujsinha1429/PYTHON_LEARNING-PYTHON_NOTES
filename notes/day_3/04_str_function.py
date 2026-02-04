#Function of strings 

name ="harry"

print(len(name))
# output:5

print(name.endswith("rry"))
# output:True

print(name.endswith("rrya"))
# output : flase 

print(name.startswith("ha"))
# output: true 

print(name.capitalize()) #capitalized the first character of the string 
# output : Harry

print(name.upper()) # uppercase the whole string 
# output: HARRY

print(name.lower()) # lower case the whole string 
# output : harry

print(name.title()) #capitalized the first character of each word in the string 
# output : HARRY

print(name.replace("harry","anujj"))
# output : anujj
