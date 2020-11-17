square = ["1","2","3","4","5","6","7","8","9"]
mark = "X"

def game():
    mark = "X"
    while True:
        draw()
        choice = int(input())
        if square[choice-1] != "X" and square[choice-1] != "O":
            if mark == "X":
                mark = "O"
            else:
                mark = "X"
            square[choice-1] = mark
            if checkwin() == 1:
                print(mark,"wins")
                break
            elif checkwin() == 2:
                print("draw")
                break
def draw():
    print("     |     |     ")
    print("  " + square[0] + "  |  " + square[1] + "  |  " + square[2])

    print( "_____|_____|_____" )
    print( "     |     |     " )

    print("  " + square[3] + "  |  " + square[4] + "  |  " + square[5])

    print( "_____|_____|_____" )
    print( "     |     |     " )

    print("  " + square[6] + "  |  " + square[7] + "  |  " + square[8])

    print("     |     |     ")
    
def checkwin():
    if square[0] == square[1] == square[2]:
        return 1
    elif square[3] == square[4] == square[5]:
        return 1
    elif square[6] == square[7] == square[8]:
        return 1
    elif square[0] == square[3] == square[6]:
        return 1
    elif square[1] == square[4] == square[7]:
        return 1
    elif square[2] == square[5] == square[8]:
        return 1
    elif square[0] == square[4] == square[8]:
        return 1
    elif square[2] == square[4] == square[6]:
        return 1
    else:
        tie = True
        for x in square:
            if x != "X" and x != "O":
                tie = False
        if tie == True:
            return 2
        
            

game()