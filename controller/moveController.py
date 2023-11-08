def getCell(board, location):
    for cell in board:
        if cell["cell"] == location:
            return cell

def move(board, origin, location):
    origin = getCell(board, origin)
    location = getCell(board, location)
    color = origin["color"]
    piece = origin["piece"]
    originSplit = list(origin["cell"])
    locationSplit = list(location["cell"])
    allowedMove = False

    if piece == "p":
        if color == "w":
            if originSplit[0] == locationSplit[0] and location["piece"] == "" and locationSplit[1] == str(int(originSplit[1]) + 1):
                allowedMove = True
            elif originSplit[0] != locationSplit[0] and location["piece"] != "" and location["color"] != color and locationSplit[1] == str(int(originSplit[1]) + 1):
                allowedMove = True
            elif originSplit[1] == "2" and locationSplit[1] == "4" and location["piece"] == ""and board[board.index(location) - 8]["piece"] == "":
                allowedMove = True
        elif color == "b":
            if originSplit[0] == locationSplit[0] and location["piece"] == "" and locationSplit[1] == str(int(originSplit[1]) - 1):
                allowedMove = True
            elif originSplit[0] != locationSplit[0] and location["piece"] != "" and location["color"] != color and locationSplit[1] == str(int(originSplit[1]) - 1):
                allowedMove = True
            elif originSplit[1] == "7" and locationSplit[1] == "5" and location["piece"] == "" and board[board.index(location) + 8]["piece"] == "":
                allowedMove = True
        if allowedMove:
            originIndex = board.index(origin)
            locationIndex = board.index(location)
            board = pawn(board, originIndex, locationIndex, color)
    elif piece == "R":
        if originSplit[0] == locationSplit[0] and originSplit[1] != locationSplit[1]:
            for cell in board:
                cellSplit = list(cell["cell"])
                if cellSplit[0] == originSplit[0] and cellSplit[1] > originSplit[1] and cellSplit[1] < locationSplit[1]:
                    if cell["piece"] != "":
                        allowedMove = False
                        break
                    else:
                        allowedMove = True
                elif cellSplit[0] == originSplit[0] and cellSplit[1] < originSplit[1] and cellSplit[1] > locationSplit[1]:
                    if cell["piece"] != "":
                        allowedMove = False
                        break
                    else:
                        allowedMove = True
        elif originSplit[1] == locationSplit[1] and originSplit[0] != locationSplit[0]:
            for cell in board:
                cellSplit = list(cell["cell"])
                if cellSplit[1] == originSplit[1] and cellSplit[0] > originSplit[0] and cellSplit[0] < locationSplit[0]:
                    if cell["piece"] != "":
                        allowedMove = False
                        break
                    else:
                        allowedMove = True
                elif cellSplit[1] == originSplit[1] and cellSplit[0] < originSplit[0] and cellSplit[0] > locationSplit[0]:
                    if cell["piece"] != "":
                        allowedMove = False
                        break
                    else:
                        allowedMove = True
        if allowedMove:
            originIndex = board.index(origin)
            locationIndex = board.index(location)
            board = rook(board, originIndex, locationIndex, color)

    elif piece == "N":
        if (abs(int(originSplit[0]) - int(locationSplit[0])) == 1 and abs(int(originSplit[1]) - int(locationSplit[1])) == 2) or (abs(int(originSplit[0]) - int(locationSplit[0])) == 2 and abs(int(originSplit[1]) - int(locationSplit[1])) == 1):
            for cell in board:
                if cell["cell"] == location["cell"] and cell["color"] != color:
                    allowedMove = True
                    break
        if allowedMove:
            originIndex = board.index(origin)
            locationIndex = board.index(location)
            board = knight(board, originIndex, locationIndex, color)

    elif piece == "B":
        if abs(int(originSplit[0]) - int(locationSplit[0])) == abs(int(originSplit[1]) - int(locationSplit[1])):
            for cell in board:
                cellSplit = list(cell["cell"])
                if cellSplit[0] > originSplit[0] and cellSplit[0] < locationSplit[0] and cellSplit[1] > originSplit[1] and cellSplit[1] < locationSplit[1]:
                    if cell["piece"] != "":
                        allowedMove = False
                        break
                    else:
                        allowedMove = True
                elif cellSplit[0] < originSplit[0] and cellSplit[0] > locationSplit[0] and cellSplit[1] < originSplit[1] and cellSplit[1] > locationSplit[1]:
                    if cell["piece"] != "":
                        allowedMove = False
                        break
                    else:
                        allowedMove = True
                elif cellSplit[0] > originSplit[0] and cellSplit[0] < locationSplit[0] and cellSplit[1] < originSplit[1] and cellSplit[1] > locationSplit[1]:
                    if cell["piece"] != "":
                        allowedMove = False
                        break
                    else:
                        allowedMove = True
                elif cellSplit[0] < originSplit[0] and cellSplit[0] > locationSplit[0] and cellSplit[1] > originSplit[1] and cellSplit[1] < locationSplit[1]:
                    if cell["piece"] != "":
                        allowedMove = False
                        break
                    else:
                        allowedMove = True
        if allowedMove:
            originIndex = board.index(origin)
            locationIndex = board.index(location)
            board = bishop(board, originIndex, locationIndex, color)

    elif piece == "Q":
        if originSplit[0] == locationSplit[0] and originSplit[1] != locationSplit[1]:
            for cell in board:
                cellSplit = list(cell["cell"])
                if cellSplit[0] == originSplit[0] and cellSplit[1] > originSplit[1] and cellSplit[1] < locationSplit[1]:
                    if cell["piece"] != "":
                        allowedMove = False
                        break
                    else:
                        allowedMove = True
                elif cellSplit[0] == originSplit[0] and cellSplit[1] < originSplit[1] and cellSplit[1] > locationSplit[1]:
                    if cell["piece"] != "":
                        allowedMove = False
                        break
                    else:
                        allowedMove = True
        elif originSplit[1] == locationSplit[1] and originSplit[0] != locationSplit[0]:
            for cell in board:
                cellSplit = list(cell["cell"])
                if cellSplit[1] == originSplit[1] and cellSplit[0] > originSplit[0] and cellSplit[0] < locationSplit[0]:
                    if cell["piece"] != "":
                        allowedMove = False
                        break
                    else:
                        allowedMove = True
                elif cellSplit[1] == originSplit[1] and cellSplit[0] < originSplit[0] and cellSplit[0] > locationSplit[0]:
                    if cell["piece"] != "":
                        allowedMove = False
                        break
                    else:
                        allowedMove = True
        elif abs(int(originSplit[0]) - int(locationSplit[0])) == abs(int(originSplit[1]) - int(locationSplit[1])):
            for cell in board:
                cellSplit = list(cell["cell"])
                if cellSplit[0] > originSplit[0] and cellSplit[0] < locationSplit[0] and cellSplit[1] > originSplit[1] and cellSplit[1] < locationSplit[1]:
                    if cell["piece"] != "":
                        allowedMove = False
                        break
                    else:
                        allowedMove = True
                elif cellSplit[0] < originSplit[0] and cellSplit[0] > locationSplit[0] and cellSplit[1] < originSplit[1] and cellSplit[1] > locationSplit[1]:
                    if cell["piece"] != "":
                        allowedMove = False
                        break
                    else:
                        allowedMove = True
                elif cellSplit[0] > originSplit[0] and cellSplit[0] < locationSplit[0] and cellSplit[1] < originSplit[1] and cellSplit[1] > locationSplit[1]:
                    if cell["piece"] != "":
                        allowedMove = False
                        break
                    else:
                        allowedMove = True
                elif cellSplit[0] < originSplit[0] and cellSplit[0] > locationSplit[0] and cellSplit[1] > originSplit[1] and cellSplit[1] < locationSplit[1]:
                    if cell["piece"] != "":
                        allowedMove = False
                        break
                    else:
                        allowedMove = True
        if allowedMove:
            originIndex = board.index(origin)
            locationIndex = board.index(location)
            board = queen(board, originIndex, locationIndex, color)

    elif piece == "K":
        if originSplit[0] == locationSplit[0] and originSplit[1] != locationSplit[1]:
            if abs(int(originSplit[1]) - int(locationSplit[1])) == 1:
                allowedMove = True
        elif originSplit[1] == locationSplit[1] and originSplit[0] != locationSplit[0]:
            if abs(int(originSplit[0]) - int(locationSplit[0])) == 1:
                allowedMove = True
        if allowedMove:
            originIndex = board.index(origin)
            locationIndex = board.index(location)
            board = king(board, originIndex, locationIndex, color)

    if allowedMove:
        return board

def pawn(board, origin, location, color):
    board[origin]["piece"] = ""
    board[origin]["color"] = ""
    if (board[location]["cell"][1] == "8" and color == "w") or (board[location]["cell"][1] == "1" and color == "b"):
        piece = input("What piece do you want to promote to? ").upper()
        if piece == "Q" or piece == "R" or piece == "B" or piece == "N":
            board[location]["piece"] = piece
    else:
        board[location]["piece"] = "p"
    board[location]["color"] = color
    return board

def rook(board, origin, location, color):
    board[origin]["piece"] = ""
    board[origin]["color"] = ""
    board[location]["piece"] = "R"
    board[location]["color"] = color
    return board

def knight(board, origin, location, color):
    board[origin]["piece"] = ""
    board[origin]["color"] = ""
    board[location]["piece"] = "N"
    board[location]["color"] = color
    return board

def bishop(board, origin, location, color):
    board[origin]["piece"] = ""
    board[origin]["color"] = ""
    board[location]["piece"] = "B"
    board[location]["color"] = color
    return board

def queen(board, origin, location, color):
    board[origin]["piece"] = ""
    board[origin]["color"] = ""
    board[location]["piece"] = "Q"
    board[location]["color"] = color
    return board

def king(board, origin, location, color):
    board[origin]["piece"] = ""
    board[origin]["color"] = ""
    board[location]["piece"] = "K"
    board[location]["color"] = color
    return board