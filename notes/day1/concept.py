a=[1,2]
b=a
c=a.copy()

b.append(3)
c.append(4)

print(a)
print(b)
print(c)
print(id(a), id(b), id(c))

# Output:
# [1,2,3]
# [1,2,3]
# [1,2,4]
# (same_id) (same_id_as_a) (different_id)
