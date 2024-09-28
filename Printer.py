from time import sleep

def print_card(card, direction):
    print("Name: The "+card.name)
    array = [["■ ","■ ","■ ","■ ","■ "],
             ["■ ","■ ","■ ","■ ","■ "],
             ["■ ","■ ","□ ","■ ","■ "],
             ["■ ","■ ","■ ","■ ","■ "],
             ["■ ","■ ","■ ","■ ","■ "]]
    for i in card.moves:
        array[(direction*(i[1])+2)][(direction*(i[0])+2)] = "▣ "
    for i in array:
        print("\t"+i[0]+i[1]+i[2]+i[3]+i[4])
    sleep(1)

def print_deck(name,deck,direction):
    print("\n"+name + "'s Deck:")
    sleep(1)
    for i in deck:
        print_card(i,direction)
    
def board(players):
    #sets empty board
    blackpawns = players[0].pieces
    whitepawns = players[1].pieces
    blackking = players[0].king
    whiteking = players[1].king
    array = [["[--]","[--]","[--]","[--]","[--]"],
             ["[--]","[--]","[--]","[--]","[--]"],
             ["[--]","[--]","[--]","[--]","[--]"],
             ["[--]","[--]","[--]","[--]","[--]"],
             ["[--]","[--]","[--]","[--]","[--]"]]
    
    #adds pieces to board based on coordinates
    for i in whitepawns:
        x = i[0]
        y = i[1]
        array[y][x] = "[♟ ]"
    for i in blackpawns:
        x = i[0]
        y = i[1]
        array[y][x] = "[♙ ]"
    if whiteking != 0:
        array[whiteking[1]][whiteking[0]] = "[♚ ]"
    if blackking != 0:
        array[blackking[1]][blackking[0]] = "[♔ ]"
    
    #prints board
    for i in range(len(array)):
        string = str(i+1) + "|"
        for j in array[i]:
            string += j
        string += "|"
        print("\t"+string)
    print("\t    a   b   c   d   e")
    sleep(1)