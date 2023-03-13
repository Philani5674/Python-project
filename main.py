import makemove

x = "X"
O = "O"
b = [" ", " ", " ", " ", " ", " ", " ", " ", " "]  #list of empty spaces for the board
player = O

#board string
board = f'{b[0]}|{b[1]}|{b[2]}   1|2|3\n-----   -----\n{b[3]}|{b[4]}|{b[5]}   4|5|6\n-----   -----\n{b[6]}|{b[7]}|{b[8]}   7|8|9'

print('Welcome to tic tac toe enjoy the funnest game ever. There are two player X and O \n\n\n')
# before the game starts print an empty board
print(f'\n\n{board}\n\n')
a =[]

while not makemove.isWinner(b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8]):
    if player == x:
        player = O
    elif player == O:
        player = x
    a = makemove.MakeMove(player, b)
    b = a[2]
    #display the new board
    makemove.displayBoard(b)
    if not (" " in b):
        print('The game ended in a tie')
        break
print(f"{a[1]} Player Won the game, Congratulations")

