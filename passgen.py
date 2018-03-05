import random
def main():
    while True:

        print "\t\tPASSWORD GENERATOR\n"
        password = ''
        length = int(input("\t\tEnter the length of your new password: "))
        characters = '@$#%&abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

        for char in range(length):
            password += random.choice(characters)
        print "\n\n\t\tYour password is" + password
        choice = raw_input("\n\n\t\tWant to generate a new password(y/n): ")
       
        if(choice == 'y'):                        
            print "\t\tHere you go.."
        elif(choice == 'n'):
            print "\n\n\t\tGoodBye!\n\n"
            return False
        else:
            print "\n\n\t\tPlease Enter a correct input "

if __name__ == "__main__":
    main()
