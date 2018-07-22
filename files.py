# write
txt = '\nThis is a test text!\n'
myFile = open('new.txt', 'w')
myFile.write(txt)
myFile.close()
# append
newtxt = 'Adding new txt to file.\n'
aText = open('new.txt', 'a')
aText.write(newtxt)
aText.close()
# read
readFile = open('new.txt', 'r').read()
print(readFile)