
def tutstart(tutorial): #Starts the tutorial if user chooses yes, procedes to game if user chooses no
    if tutorial == "N":
        print("You have selected NO")
    
    elif tutorial == "Y":
        print("You have selected YES")
    
    else:
        while tutorial != "Y" and tutorial != "N":
            print("That is not a valid answer, try again")
            tutorial = input().upper()
            
            if tutorial == "N":
                print("You have selected NO")
            
            elif tutorial == "Y":
                print("You have selected YES")
                printboard()
                
def printboard(L1, L2): #Function responsible for printing board updates
    print("Player 1 Side")
    print(("|" +("-" * 5))*6 + "|") #prints top row of the board
    for i in range(len(L1)): #prints Player 1 seeds
        print("|" +(" " * 2 + str(L1[i]) + " " * 2), end = "")
    print("|", end = "") #prints last line on row with seed values
    print()
    print("|" + (("-" * 5) + "|") * 6) #prints middle row of board
    for i in range(len(L2)):
        print("|" +(" " * 2 + str(L2[i]) + " " * 2), end = "")
    print("|", end = "") #prints last line on row with seed values
    print()
    print(("|" +("-" * 5))*6 + "|") #prints bottom row of the board
    print("Player 2 Side")
    print()
    
if __name__ == "__main__":

    print("Hello! Welcome to the game of Oware!")
    print("Would you like to start the tutorial? (Y/N)")
    tanswer = input().upper()
    
    tutstart(tanswer) #start the tutorial
    print()
    
    p1seeds = [4, 4, 4 ,4 ,4, 4]
    p2seeds = [4, 4, 4 ,4 ,4, 4]
    
    printboard(p1seeds, p2seeds)
    
