import copy

a=[[1, 2], [3, 4]]

b=copy.deepcopy(a)
b[0].append(99)

print(a)
print(b)

# Output:
# a=[[1, 2], [3, 4]]
# b=[[1, 2, 99], [3, 4]]
# deepcopy har level pai new object bana deta hai.
