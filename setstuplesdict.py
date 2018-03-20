#A tuple stores multiple FIXED constant values in a sequence
#A set stores multiple UNIQUE values in an unordered collection
#A dictionary stores multiple unordered values in key:value pairs
asia = ('India', 'Japan', 'China')#tuple
print '\n\t\tTuple: ', asia, '\tLength: ', len(asia), '\tType: ', type(asia)

planets = {'Earth', 'Jupiter', 'Mars'}#set
print '\n\t\tSet: ', planets
planets.add('Venus')
print '\n\t\tUpdated Set: ', planets
print '\n\t\tIs Venus in planets set: ', 'Venus' in planets

planets2 = {'Mars', 'Earth'}
print '\n\t\tSet 2 : ', planets2
print '\n\t\tCommon in both sets : ', planets.intersection(planets2)

students = {'1':'Bob', '2':'Alice', 'new':'Raj'}#dictionary
print '\n\t\tDictionary: ', students
print '\n\t\tnew : ', students['new']
print '\n\t\tAll keys: ', students.keys()
del students['1']
print '\n\t\tAfter Deleting: ', students
print '\n\t\tIs there a \'1\' key in dictionary? : ', '1' in students 
students['old'] = 'Jay'
print '\n\t\tUpdated Dictionary : ', students, '\n'
