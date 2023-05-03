#Tic Tac Toe Game!
import random
import os

player = "X"
computer = "O"

game = True

combinations = [
    ("1", "2", "3"),  # top row
    ("4", "5", "6"),  # middle row
    ("7", "8", "9"),  # bottom row
    ("1", "4", "7"),  # left column
    ("2", "5", "8"),  # middle column
    ("3", "6", "9"),  # right column
    ("1", "5", "9"),  # diagonal from top-left to bottom-right
    ("3", "5", "7"),  # diagonal from top-right to bottom-left
]

def print_board():
    one = board_spaces["1"]
    two = board_spaces["2"]
    three = board_spaces["3"]
    four = board_spaces["4"]
    five = board_spaces["5"]
    six = board_spaces["6"]
    seven = board_spaces["7"]
    eight = board_spaces["8"]
    nine = board_spaces["9"]
               
    board = f"""
     {one} | {two} | {three}
    -----------
     {four} | {five} | {six}
    -----------
     {seven} | {eight} | {nine}
    """
    print(board)

while True:
    
    os.system('clear')
    print("Tic Tac Toe Game by Pablo!")
    
    board_spaces = {"1" : " ", "2":  " ", "3" : " ",
                    "4" : " ", "5" : " ", "6" : " ",
                    "7" : " ", "8" : " ", "9" : " "}
    
    initial_board = """
     1 | 2 | 3   
    -----------
     4 | 5 | 6
    -----------
     7 | 8 | 9
    """
    print(initial_board)

    while game == True:

        player_space = str(input("Choose an empty space (1-9):"))
        computer_space = str(random.randint(1,9))
        os.system('clear')
        
        while True:
            if player_space in board_spaces and board_spaces[player_space] == " ":
                board_spaces[str(player_space)] = player
                break
            else:    
                os.system('clear')
                print("That is not a valid input, try again!")
                print_board()    
                player_space = str(input("Choose an empty space (1-9):"))
                os.system('clear')
       
        for combination in combinations:
            
            if board_spaces[combination[0]] == board_spaces[combination[1]] == board_spaces[combination[2]] == "X":
                print("You Win!")
                game = False
                break

            elif board_spaces[combination[0]] == board_spaces[combination[1]] == board_spaces[combination[2]] == "O":
                print("You lose!")
                game = False
                break
            
        if game == False:
            print_board()
            break
       
        if any(value not in ["X", "O"] for value in board_spaces.values()):            
            
            while True:
                if board_spaces[computer_space] == " ":
                    board_spaces[str(computer_space)] = computer
                    break
                else:
                    computer_space = str(random.randint(1,9))
            
        else:
            print("Draw!")
            print_board()
            break
        
        for combination in combinations:
            
            if board_spaces[combination[0]] == board_spaces[combination[1]] == board_spaces[combination[2]] == "X":
                print("You Win!")
                game = False
                break

            elif board_spaces[combination[0]] == board_spaces[combination[1]] == board_spaces[combination[2]] == "O":
                print("You lose!")
                game = False
                break
            
        if game == False:
            print_board()
            break
        
        print_board()
            
    replay = input("Do you want to play again? y/n: ")
    if replay == "y":
        game = True
        continue
    elif replay == "n":
        print("\nThanks for playing!")
        break
    else:
        print("\nYeet!")
        break