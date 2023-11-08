import csv
import os

def getBoard(name):
    if name == "new":
        with open("saves/defaultBoard.csv", "r", encoding="UTF-8") as f:
            return list(csv.DictReader(f))
    with open(f"saves/{name}.csv", "r", encoding="UTF-8") as f:
        boardList = list(csv.DictReader(f))
    return boardList

def getBoardList():
    with open("saves/savedBoards.csv", "r", encoding="UTF-8") as f:
        boardList = list(csv.DictReader(f))
    return boardList
    
def showBoards():
    with open("saves/savedBoards.csv", "r", encoding="UTF-8") as f:
        boardList = list(csv.DictReader(f))
    for board in boardList:
        print("Name: " + board["boardName"])
        print("To move:" + board["toMove"])
        print("Turn: " + board["turn"] + "\n")

def saveBoard(board, name, toMove, turn):
    existingBoards = getBoardList()
    for existingBoard in existingBoards:
        if existingBoard["boardName"] == name:
            existingBoards.remove(existingBoard)
            break
    existingBoards.append({"boardName": name, "toMove": toMove, "turn": turn})
    with open("saves/savedBoards.csv", "w", encoding="UTF-8") as f:
        f.write("boardName,toMove,turn\n")
        for existingBoard in existingBoards:
            f.write(f"{existingBoard['boardName']},{existingBoard['toMove']},{existingBoard['turn']}\n")
    with open(f"saves/{name}.csv", "w", encoding="UTF-8") as f:
        f.write("cell,piece,color\n")
        for piece in board:
            f.write(f"{piece['cell']},{piece['piece']},{piece['color']}\n")