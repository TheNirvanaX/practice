# chess board validator program
position=[] #valid positon
for i in range(1,9):
    for j in ["a","b","c","d","e","f","g","h"]:
        x=str(i)+j
        position.append(x)

pieces=[] #valid pieces
for i in ["w","b"]:
    for j in ["king","queen","bishop","knight","pawn","rook"]:
        x=i+j
        pieces.append(x)

board= {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

def isValidChessboard(dict):
    count={}
    for pos,pice in dict.items(): # this loop counts pieces
        if pos in position:
            count.setdefault(pice,0)
            count[pice]+=1
    
        else:
            return "False"
    print(count)
    ans="False"
    for key in count:
        if (key=="wpawn" or key=="bpawn") and count[key]>8:
            ans="False"
            break
        elif (key=="bking" or key=="wking" or key=="bqueen" or key=="wqueen") and count[key]>1:
            ans="False"
            break
        elif (key=="wknight" or key=="wrook" or key=="wbishop" or key=="bknight" or key=="brook" or key=="bbishop") and count[key]>2:
            ans="False"
            break
        else:
            ans="True"
    return ans

print(isValidChessboard(board))