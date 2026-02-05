friends=["apple","orange",5,345.65,False,"akash","rohan"]
print(friends)
# output:['apple', 'orange', 5, 345.65, False, 'akash', 'rohan'

friends.append("harry")
print(friends)
# output:['apple', 'orange', 5, 345.65, False, 'akash', 'rohan', 'harry']    #this is because list is mutable..

l1=[3,1,9,5,3,2,6,5,7]
l1.sort()
print(l1) 
# output: [1, 2, 3, 3, 5, 5, 6, 7, 9] #sort() will return a sorted list 

l1.reverse()
print(l1)
# output: [9, 7, 6, 5, 5, 3, 3, 2, 1] #It will reverse the list 

l1.insert(3,"anuj")
print(l1)
# output: [9, 7, 6, 'anuj', 5, 5, 3, 3, 2, 1] # insert() help to insert anything inside a list 

l1.pop(3)
print(l1)
# output: 9, 7, 6, 5, 5, 3, 3, 2, 1] # pop() will delete the element present at that perticular index..

# if we want to print the pop element we have to do simple print statement ,
print(l1.pop(3))
# output: 5 #because after poping at index 3 "5" is present so now "5" will print
