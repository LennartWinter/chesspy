import controller.csvController as csvController
import controller.moveController as moveController
import view.main as view
import os
os.system("cls")
boards = csvController.showBoards()
boardChosen = input("Choose a board to load: ")
board = csvController.getBoard(boardChosen)
toMove = "w"
turn = 0
boardsList = csvController.getBoardList()
for b in boardsList:
    if b["boardName"] == boardChosen:
        toMove = b["toMove"]
        turn = int(b["turn"])
        break

isRunning = True

while isRunning:
    os.system("cls")
    view.showBoard(board)
    move = input("Enter a move: ")
    if move == "exit":
        isRunning = False
    elif move == "reset":
        board = csvController.getBoard(boardChosen)
    elif move == "save":
        if boardChosen == "new":
            boardChosen = input("Enter a name for the board: ")
            csvController.saveBoard(board, boardChosen, toMove, turn)
        else:
            csvController.saveBoard(board, boardChosen, toMove, turn)
    else:
        move = move.split(" ")
        moveController.move(board, move[0], move[1])
    turn += 1