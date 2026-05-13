import os
players={}
player_x=input("Jméno hráče X: ")
players[player_x]="X"
player_o=input("Jméno hráče O: ")
players[player_o]="O"

size=int(input("Zadej rozměr N: "))
win_len=int(input("Zadej počet v řadě K: "))

board=[]
for i in range(size):
    line=[]
    for i in range(size):
        line.append(".")
    board.append(line)

def show_board():
    index=1
    print("  ",end="")
    for i in range(size):
        print(i+1,end=" ")
    print("")
    for line in board:
        print(index,end=" ")
        for place in line:
            print(place,end=" ")
        print("")
        index+=1

def place(player, row, column):
    if board[row-1][column-1] == ".":
        print(f"Označen sloupec {column} a řádek {row}")
        board[row-1][column-1] = players[player]
        return True
    else:
        print("Pole je už obsazené!")
        return False

def winner_check():
    vectors=[[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
    for row in board:
        row_num=0
        for place in row:
            column_num=0
            if place != ".":
                value=place
                streak=1
                for vector in vectors:
                    while board[row_num+vector[0]][column_num+vector[1]] == value:
                        streak+=1
                        row_num+=vector[0]
                        column_num+=vector[1]
                        if streak >= win_len:
                            if place=="X":
                                return player_x
                            elif place=="O":
                                return player_o                    
        row_num+=1

current_player=player_x
current_round=1
winner=None

while winner == None:
    print(f"Hráč X: {player_x}")
    print(f"Hráč O: {player_o}", end="\n")
    
    print(f"Tah {current_round} - {current_player} ({players[current_player]})", end=". ")
    user_input=input("Zadej sloupec a řádek: ")
    user_input=user_input.split()
    for i in range(len(user_input)):
        user_input[i-1]=int(user_input[i-1])

    print(user_input)
    show_board()
    place(current_player, user_input[1], user_input[0])
    if current_player==player_x:
        current_player=player_o
    else:
        current_player=player_x
    show_board()
    winner=winner_check()

print(f"Vítěž je: {winner}")