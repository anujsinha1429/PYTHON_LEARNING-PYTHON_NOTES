def modify(x):
    x.append(99)

a=[1, 2, 3]
modify(a)

print(a)  # Output: [1, 2, 3, 99]
print(id(a))  # Output: (same_id_as_before)