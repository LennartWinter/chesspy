WHITE = '\033[97m'
BLACK = '\033[30m'
END = '\033[0m'

def showBoard(board):
    print("   A B C D E F G H")
    for i in range(8):
        print(str(i + 1) + " |", end="")
        for j in range(8):
            if board[i * 8 + j]["piece"]:
                if board[i * 8 + j]["color"] == "w":
                    print(WHITE + board[i * 8 + j]["piece"] + END + "|", end="")
                else:
                    print(BLACK + board[i * 8 + j]["piece"] + END + "|", end="")
            else:
                print("_|", end="")
        print(" " + str(i + 1))
    print("   A B C D E F G H")