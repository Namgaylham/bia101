#creation of array
array1 = [1,2,3,4,"thimphu",2.5]

print(array1)
#retrieving
elememt1 = array1[0]
element2 = array1[4]
print(element2)
print(elememt1)

#negative indexing
lastElement = array1[-5]


print(lastElement)
#modifying the elements
array1[0] = 10
print(array1)
#getting number of element in the array
no_of_elements = len(array1)
print(no_of_elements)

#slicing 
elements = array1[0:2]
#print(elements)
arr1 = [1,10]
arr2 = ['thimphu','wangdue']
arr3 = arr1 + arr2
print(arr3)
number_to_check = 2
result = number_to_check in arr1
print("result is",result)


arrvariable = [1,2,3]

arrvariable.append(4)
print(arrvariable)
#inserting at a specific index
arrvariable.insert(1,10)
print(arrvariable)
arrvariable.sort()
print(arrvariable)
stackvar = []
#adding to stack
stackvar.append(4)
stackvar.append(2)
stackvar.append(9)
stackvar.append(1)
print('after appending',stackvar)
element = stackvar.pop()
print('after poping',stackvar)
print('removed element',element)

