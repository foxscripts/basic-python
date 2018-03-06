#def main():
#    while True:
alphabets = {'a':'z', 'b':'y', 'c':'x', 'd':'w', 'e':'v', 'f':'u', 'g':'t', 'h':'s', 'i':'r',
                'j':'q', 'k':'p',  'l':'o', 'm':'n', 'n':'m', 'o':'l','p':'k', 'q':'j',
                'r':'i', 's':'h', 't':'g', 'u':'f', 'v':'e', 'w':'d', 'x':'c', 'y':'b', 'z':'a'} 
message = raw_input("\n\tPlease enter your message: ").lower()
encryMessage = ''
for alphabet in message:
        if alphabet in alphabets:
            encryMessage += alphabets[alphabet]
        else:
            encryMessage += alphabet
print "\n\t" + encryMessage + "\n"
#        choice = raw_input("\n\n\t\tWant to generate a new encrypted message(y/n): ")
       
#        if(choice == 'y'):                        
#            print "\t\tHere you go.."
#        elif(choice == 'n'):
#            print "\n\n\t\tGoodBye!\n\n"
#            return False
#        else:
#            print "\n\n\t\tPlease Enter a correct input "

#if __name__ == " __main__":
#	main() 
