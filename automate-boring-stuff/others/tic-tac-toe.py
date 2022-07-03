# this is a program for tic-tac-toe game
import sys

# create dict for storing values
dict={}
position=["top-L","top-M","top-R",
    "mid-L","mid-M","mid-R",
    "bottom-L","bottom-M","bottom-R"]
for place in position:
    dict.setdefault(place," ")

# custom print function for display board
def printdict():
    print(" "+dict["top-L"]+" "," "+dict["top-M"]+" "," "+dict["top-R"]+" ",sep="|")
    print("---+---+---")
    print(" "+dict["mid-L"]+" "," "+dict["mid-M"]+" "," "+dict["mid-R"]+" ",sep="|")
    print("---+---+---")
    print(" "+dict["bottom-L"]+" "," "+dict["bottom-M"]+" "," "+dict["bottom-R"]+" ",sep="|")


def winner(): # decide winner!
    if dict["top-L"]==dict["top-M"] and dict["top-L"]==dict["top-R"] and dict["top-L"] != " ":#top row
        print("Hurraay! player "+dict["top-L"]+" wins.")
        sys.exit()
    elif dict["mid-L"]==dict["mid-M"] and dict["mid-L"]==dict["mid-R"] and dict["mid-L"] != " ":# mid row
        print("Hurraay! player "+dict["mid-L"]+" wins.")
        sys.exit()
    elif dict["bottom-L"]==dict["bottom-M"] and dict["bottom-L"]==dict["bottom-R"] and dict["bottom-L"] != " ":# bottom row
        print("Hurraay! player "+dict["bottom-L"]+" wins.")
        sys.exit()   
    elif dict["top-L"]==dict["mid-M"] and dict["top-L"]==dict["bottom-R"] and dict["top-L"] != " ":# prime diagonal
        print("Hurraay! player "+dict["top-L"]+" wins.")
        sys.exit()   
    elif dict["top-R"]==dict["mid-M"] and dict["top-R"]==dict["bottom-L"] and dict["top-R"] != " ":# secondary diagonal
        print("Hurraay! player "+dict["top-R"]+" wins.")
        sys.exit()   
    elif dict["top-L"]==dict["mid-L"] and dict["top-L"]==dict["bottom-L"] and dict["top-L"] != " ":# column 1
        print("Hurraay! player "+dict["top-L"]+" wins.")
        sys.exit()   
    elif dict["top-M"]==dict["mid-M"] and dict["top-M"]==dict["bottom-M"] and dict["top-M"] != " ":# column 2
        print("Hurraay! player "+dict["top-M"]+" wins.")
        sys.exit()  
    elif dict["top-R"]==dict["mid-R"] and dict["top-R"]==dict["bottom-R"] and dict["top-R"] != " ":# column 3
        print("Hurraay! player "+dict["top-R"]+" wins.")
        sys.exit()
    else:
        pass



#player input move
turn="X"
for _ in range(9): # main loop
    printdict()
    winner()
    print("Turn for "+turn+". Move on which space ?")
    move=input()
    dict[move]=turn
    if turn=="X":
        turn="O"
    elif turn=="O":
        turn="X"
    
