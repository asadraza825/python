import random

def DisplayBoard(board):
    print("+--------+--------+--------+")
    print("|   "+str(board['1'])+"    |   "+str(board['2'])+"    |   "+str(board['3'])+"    |")
    print("+--------+--------+--------+")
    print("|   "+str(board['4'])+"    |   "+str(board['5'])+"    |   "+str(board['6'])+"    |")
    print("+--------+--------+--------+")
    print("|   "+str(board['7'])+"    |   "+str(board['8'])+"    |   "+str(board['9'])+"    |")
    print("+--------+--------+--------+")


def EnterMove(board):
    if(MakeListOfFreeFields(board)>0):
        while True:    
            move = input("Please enter your move: ")
            if move in board and board[move]!= "X" and board[move] != "O":
                 board[move] = "O"
                 break
            else:
                 print("Slot already selected or you have entered wrong number")
                 MakeListOfFreeFields(board)
        DisplayBoard(board)

def MakeListOfFreeFields(board):
    available = 0
    for key,value in board.items():
        if value !="X" and value !="O":
             print("Available moves =>"+str(key))
             available +=1
    return available        

def VictoryFor(board, sign):
    vict = 0
    if board['1'] == sign and   board['2'] == sign and board['3'] == sign:
        vict +=1
    if board['4'] == sign and board['5'] == sign and board['6'] == sign:
        vict +=1
    if board['7'] == sign and board['8'] == sign and board['9'] == sign:
        vict +=1
    if board['1'] == sign and board['4'] == sign and board['7'] == sign:
        vict +=1
    if board['1'] == sign and board['5'] == sign and board['9'] == sign:
        vict +=1
    if board['2'] == sign and board['5'] == sign and board['8'] == sign:
        vict +=1
    if board['3'] == sign and board['6'] == sign and board['9'] == sign:
        vict +=1
    return vict

def DrawMove(board):
    if(MakeListOfFreeFields(board)>0):
        move = str(random.randint(1,9))
        while True:
            if board[move]!= "X" and board[move] != "O":
                board[move] = "X"
                break
            else:
                move = str(random.randint(1,9))
        DisplayBoard(board)

board = {'1':'1','2':2,'3':3,'4':4,'5':"X",'6':6,'7':7,'8':8,'9':9}
move = "X"
DisplayBoard(board)
for i in range(8):
     EnterMove(board)
     DrawMove(board) 
     
user = VictoryFor(board,"O")
computer = VictoryFor(board,"X")
if user == computer:
    print("Mathc Ties!")
elif user>computer:
    print("Congrats! you win!")
elif user<computer:
    print("Oh! you loss")      