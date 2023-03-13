
def MakeMove(player, spaceslist):
    currentplayer = player
    #choose the space from the board that is empty
    move = int(input(f"Player {currentplayer} choose the space you want to fill numbers from 1-9:\n>>>"))

    #check if the space is empty and between 1 and 9, including 1 and 9
    while not (move in [1, 2, 3, 4, 5, 6, 7, 8, 9] and spaceslist[move-1] == " "):
        move = int(input(f"Player {currentplayer} choose the space you want to fill numbers from 1-9:\n>>>"))

    #making the selection in the list if the space is empty and entered correctly
    spaceslist[move-1] = currentplayer

    #returns a list of player move index and currentplayer(X or O) and the updated list of all the spaces
    return [move, currentplayer, spaceslist]


def isWinner(a, b, c, d, e, f, g, h, i):
    #Checks if there is a winner in the game
    return ((a == b == c == "X" or d == e == f == "X") or (g == h == i == "X" or c == e == g == "X") or\
         (a == e == i == "X" or a == d == g == "X") or (b == e == h == "X" or c == f == i == "X") or \
         (a == b == c == "O" or d == e == f == "O") or (g == h == i == "O" or c == e == g == "O") or \
         (a == e == i == "O" or a == d == g == "O") or (b == e == h == "O" or c == f == i == "O"))


def displayBoard(x):
    b = x
    board = f'{b[0]}|{b[1]}|{b[2]}   1|2|3\n-----   -----\n{b[3]}|{b[4]}|{b[5]}   4|5|6\n-----   -----\n{b[6]}|{b[7]}|{b[8]}   7|8|9'
    print(f'\n\n{board}\n\n')