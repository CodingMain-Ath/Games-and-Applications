def intro():
    pass #for now just

    print ("\nWelcome to the traditional game of tic tac toe. The rules remain the same. \nYour num-pad will act as ur tic tac toe board.")
    print ("\nSelect the number corresponding to the place where you want to place your marker.")
    print ("Player 1: X \nPlayer 2: O")
    print ("\n \nLet's Begin!!!")
    print ("May the best player win!")


#essentials
global display_list
display_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

from IPython.display import clear_output

def move_display():
    
    board_display1 = " " + display_list[6] + "|" + display_list[7] + "|" + display_list[8]
    board_display2 = " " + display_list[3] + "|" + display_list[4] + "|" + display_list[5]
    board_display3 = " " + display_list[0] + "|" + display_list[1] + "|" + display_list[2]

    print (board_display1)
    print ("-------")
    print (board_display2)
    print ("-------")
    print (board_display3)
    print ("\n")
    
def input_from_user():

    inplace_list = [1,2,3,4,5,6,7,8,9]

    condition_needed = False
    global place_number

    while condition_needed == False:
        place_number = input("Input the corresponding number from your keypad: ")

        if place_number.isdigit():
            
            place_number = int(place_number)
            
            condition_needed2 = False
            while condition_needed2 == False:
                if place_number in inplace_list:
                    condition_needed2 = True
                    condition_needed = True
                    break
                else:
                    print ("Integer not in keypad range")
                    condition_needed2 = False
                    condition_needed = False
                    break
            

        else: 
            print ("Enter Valid Number!")
            condition_needed = False  

    return place_number 

def working_X():
    input_from_user()
    clear_output()
    display_list[place_number-1] = "X"
    move_display()
    
def working_O():
    input_from_user()
    clear_output()
    display_list[place_number-1] = "O"
    move_display()

def clarity():
    ans = input("Press 'y' to begin!")

    while ans != "y":
        ans = input("Press 'y' to begin!")

def game_mech():

    intro()
    move_display()
    clarity()
    clear_output()

    condition = False

    while condition == False:
    
        working_X()
        #Player 1 i.e. X
        if display_list[0] == display_list[1] == display_list[2] == "X":
            print("Game Over!")
            print("Player 1 wins!!!")
            condition = True
            break

        elif display_list[3] == display_list[4] == display_list[5] == "X":
            print("Game Over!")
            print("Player 1 wins!!!")
            condition = True
            break

        elif display_list[6] == display_list[7] == display_list[8] == "X":
            print("Game Over!")
            print("Player 1 wins!!!")
            condition = True
            break

        elif display_list[0] == display_list[3] == display_list[6] == "X":
            print("Game Over!")
            print("Player 1 wins!!!")
            condition = True
            break

        elif display_list[1] == display_list[4] == display_list[7] == "X":
            print("Game Over!")
            print("Player 1 wins!!!")
            condition = True
            break

        elif display_list[2] == display_list[5] == display_list[8] == "X":
            print("Game Over!")
            print("Player 1 wins!!!")
            condition = True
            break

        elif display_list[0] == display_list[4] == display_list[8] == "X":
            print("Game Over!")
            print("Player 1 wins!!!")
            condition = True
            break

        elif display_list[2] == display_list[4] == display_list[6] == "X":
            print("Game Over!")
            print("Player 1 wins!!!")
            condition = True
            break
        
        elif " " not in display_list:
            print("Game Over!")
            print("Tie!")
            condition = True
            break

        else: 
            condition = False


        working_O()
        #Player 2 i.e. O
        if display_list[0] == display_list[1] == display_list[2] == "O":
            print("Game Over!")
            print("Player 2 wins!!!")
            condition = True
            break

        elif display_list[3] == display_list[4] == display_list[5] == "O":
            print("Game Over!")
            print("Player 2 wins!!!")
            condition = True
            break

        elif display_list[6] == display_list[7] == display_list[8] == "O":
            print("Game Over!")
            print("Player 2 wins!!!")
            condition = True
            break

        elif display_list[0] == display_list[3] == display_list[6] == "O":
            print("Game Over!")
            print("Player 2 wins!!!")
            condition = True
            break

        elif display_list[1] == display_list[4] == display_list[7] == "O":
            print("Game Over!")
            print("Player 2 wins!!!")
            condition = True
            break

        elif display_list[2] == display_list[5] == display_list[8] == "O":
            print("Game Over!")
            print("Player 2 wins!!!")
            condition = True
            break

        elif display_list[0] == display_list[4] == display_list[8] == "O":
            print("Game Over!")
            print("Player 2 wins!!!")
            condition = True
            break

        elif display_list[2] == display_list[4] == display_list[6] == "O":
            print("Game Over!")
            print("Player 2 wins!!!")
            condition = True
            break

        else:
            condition = False

game_mech()
