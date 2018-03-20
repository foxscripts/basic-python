names = ['hi', 'bye', 'namaste','hi']
numbers =  [1, 2, 3]
print '\t\tNames : ', names
print '\t\tNumbers : ', numbers
names.append('yo')#added at last position
print '\t\tItem appended: ', names
numbers.insert(0, 5)#5 value is inserted at position 0
print '\t\t5 inserted at position[0]:',  numbers
numbers.remove(5)#removes first 5 value in list
print'\t\t5 removed:', numbers
print '\t\tThe item removed from names is: ' ,names.pop(1) #removes value at index 1 and return a value
print '\t\tThe number of times \'hi\' is in list : ', names.count('hi')
numbers.sort()
print '\t\tSorted numbers: ', numbers
