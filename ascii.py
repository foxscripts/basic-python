# py script to print the ASCII value of input key

def ascii():
    inputKey = raw_input("\n\n\tEnter a key whose ASCII value you want: ")
    print "\n\n\tThe ASCII value of",inputKey,"is",ord(inputKey),"\n\n"
ascii()
choice = raw_input("\tDo you want to continue (y) ")
if(choice == 'y'):
    ascii()
else:
    print "\n\n\tGoodBye :)"
