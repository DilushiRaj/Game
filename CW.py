import random
import datetime

# initializing the variables
fo = None 
comp_pos = []
human_pos = []
comp_moves = []
human_moves = []
comp_black_hole = 0
human_black_hole = 0
comp_position = 0
human_position = 0
move = 0
win = 0
win1 = 0
win3 = ["Computer won", "Computer lost"]
win4 = ["Human won", "Human lost"]
total_moves = 0
board_size = 20
comp = False
human = False
board = [
    ["1", "2", "3", "4", "5", "6", "O", "8", "9", "10", "11", "12", "13", "O", "15", "16", "17", "18", "19","20","Won"],
    ["1", "2", "3", "4", "5", "6", "O", "8", "9", "10", "11", "12", "13", "O", "15", "16", "17", "18","19","20","Won"]
]

# functions
def f1(c, h):
    comp_pos.append(c)
    human_pos.append(h)
    
def dice():
    global dice_roll         # assigning the global variables 
    dice_roll = random.randint(1, 6)
    #print(dice_roll)

def calculate_moves(dice_roll):
    global move             # assigning the global variables 
    move = dice_roll/2
    move = int(move)
    #print(move)

def black_hole(comp_position, human_position):
    # assigning the global variables 
    global comp_black_hole
    global human_black_hole
    if comp_position == 7 or comp_position == 14:
        comp_black_hole = comp_black_hole + 1               # if the computer hits the black hole it will be added as a count
    if human_position == 7 or human_position == 14:
        human_black_hole = human_black_hole + 1             # if the human hits the black hole it will be added as a count
                
def start_game():
    # assigning the global variables 
    global comp_position
    global human_position
    global comp
    global human
    global win
    global win1
    
    while comp_position < 20 and human_position < 20:
        comp_dice = random.randint(1, 6)
        human_dice = random.randint(1, 6)

        if comp_dice == 6 and comp_position == 0:   # computer can start the game
            print("Computer dice roll is 6 and can start the game")
            comp = True
        if human_dice == 6 and human_position == 0:    # human can start the game
            print("Human dice roll is 6 and can start the game")
            human = True
            pass

        if human == True:
            dice()
            calculate_moves(dice_roll)           
            human_position = human_position + move
            human_moves.append(move)
            print("Human position", human_position)
            black_hole(comp_position, human_position)
            if human_position == 7 or human_position == 14:
                human_position = 1
            if human_position >= 20:
                win = win4[0]
            else:
                win1 = win4[1]

        if comp == True:
            dice()
            calculate_moves(dice_roll)
            comp_position = comp_position + move
            comp_moves.append(move)
            f1(comp_position, human_position)
            print("Computer position", comp_position)
            black_hole(comp_position, human_position)
            if comp_position == 7 or comp_position == 14:
                comp_position = 1
            if comp_position >= 20:
                win = win3[0]
            else:
                win1 = win3[1]
                
        # displaying the grid
        for i in range(1, board_size + 1):
                print(i, end="      ")
        print()
        for x in range(2):
            def length():
                print(
                    "____________________________________________________________________________________________________________________________________________")

            length()
            for j in range(20):
                if board[x][j] == "O":
                    print("_ O _", end=" |")
                elif x == 0 and j == human_position - 1:
                    print("_ X _", end=" |")
                elif x == 1 and j == comp_position - 1:
                    print("_ X _", end=" |")
                else:
                    print("______", end="|")
            print("\n")
   
def final_output():
    print("""Human
Black hole hits: """ , human_black_hole)
    print("Total moves: ", len(human_moves))
    if win == win4[0]:
        print(win)
    elif win1 == win4[1]:
        print(win1)
    print("\n")
    print("""Computer
Black hole hits: """ , comp_black_hole)
    print("Total moves: ", len(comp_moves))
    if win == win3[0]:
        print(win)
    elif win1 == win3[1]:
        print(win1)

print("Welcome to 20X2 game")       
# calling the functions       
start_game()
final_output()

v = datetime.datetime.now()
YYYY = v.year
M = v.month
D = v.day
H = v.hour
m = v.minute

# writing the output in the text file
with open(f"{YYYY}_{M}_{D}_{H}_{m}.txt", "x") as fo:
    fo.write("Human\n")
    fo.write(f"Black hole hits:  {human_black_hole}\n")
    fo.write(f"Total moves: {len(human_moves)}\n")
    if win == win4[0]:
        fo.write(win)
    elif win1 == win4[1]:
        fo.write(win1)
    fo.write("\nComputer\n")
    fo.write(f"Black hole hits: {comp_black_hole}\n")
    fo.write(f"Total moves: {len(comp_moves)}\n")
    if win == win3[0]:
        fo.write(win)
    elif win1 == win3[1]:
        fo.write(win1)


