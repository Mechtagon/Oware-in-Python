
def intro():
    print("Hello! Welcome to the game of Oware!")
    print("Would you like to start the tutorial? (Y/N)")
    tanswer = input().upper() #Does the player want to start the tutorial?
    
    if tanswer == "N":
        print("You have selected NO")
    
    elif tanswer == "Y":
        print("You have selected YES")
    
    else:
        while tanswer != "Y" and tanswer != "N":
            print("That is not a valid answer, try again")
            tanswer = input().upper()
            
            if tanswer == "N":
                print("You have selected NO")
            
            elif tanswer == "Y":
                print("You have selected YES")
                
def printboard():
    

if __name__ == "__main__":
    intro()
