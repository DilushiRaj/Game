import random
name = input("Please enter your name : ")               # Get input name from user
print(f"Hi {name}, Welcome to GameInt")             # Display Greeting

# Generate Random colored pegs
namelist = random.sample(range(1, 6), 4)
#print(namelist)
x = 1         # x is int he places of guess
print("Number of guess",x, "\t\t\t\t", "Colour Mapping: 1- White, 2- Blue, 3- Red, 4-Yellow, 5- Green, 6- Purple")
while (x<=8):
    user_guess = []
    total_pegs = []

    for i in range(4):
        num = int(input("Enter the numbers: "))
        user_guess.append(num)
        if (num==0000):
            print("Thanks for playing the game!!")
            break


        if (num<=6):
                # correct position and has correct colour
                if namelist[i] == user_guess[i]:
                    print("1 - correct position and correct colour")
                    total_pegs.append(1)

                # wrong position but correct color
                else:
                    for j in range(len(namelist)):
                        if namelist[j] == user_guess[i]:
                            print("0 - wrong position but correct color")
                            total_pegs.append(0)

                # wrong position and colour
                if (user_guess[i] not in namelist):
                    print("- = wrong position and wrong colour")
        else:
            print("invalid number")
            break
    print("Attempt No:", "\t\t", "Guess:", "\t\t", "Result:")
    print(x, "\t\t\t\t", user_guess, "\t\t\t", total_pegs)

    # check whether the user won the game
    winning_Pegs = 0
    for k in total_pegs:
        if(k==1):
            winning_Pegs+=1
        else:
            continue
    if winning_Pegs==4:
        print("Congratulations, You won the game!!!")
        choice = input("Do you want to play the game?? (y/n): ")
        if choice.casefold() == 'n':
            print("end game")
            break
        else:
            continue
    else:
        print("Better luck next time")
        print(f"It's your {x} attempt out of 8")

    print(f"You have scored : {winning_Pegs} points.")
    x = x+1
