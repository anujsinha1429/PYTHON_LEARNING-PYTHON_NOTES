marks={
    "anuj":100,
    "shivam":200,
    "rohan":20
}

# methods:
# 1 .items()
print(marks.items()) #output: dict_items([('anuj', 100), ('shivam', 200), ('rohan', 20)])

# 2 .keys()
print(marks.keys()) #output: dict_keys(['anuj', 'shivam', 'rohan'])

# 3 .value()
print(marks.values()) #output: dict_values([100, 200, 20])

# 4 .update()
print(marks.update({"anuj":95})) 
print(marks) #output: {'anuj': 95, 'shivam': 200, 'rohan': 20}

# 5 .get()
print(marks.get("shivam")) # if key will not exist it will give error 
print(marks["shivam"]) # but here if key will not exist it will give u error

print(marks.pop("anuj")) #output: 95
# after poping the dic will become like this :
print(marks)
# output: {'shivam': 200, 'rohan': 20}

# to make empty dictionary :
d={} #that's it

