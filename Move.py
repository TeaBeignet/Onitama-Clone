from Printer import*

def win(string: str, players: list):
    print("\n"+ string + " wins!")
    board(players)
    exit()

def tile_to_cord(string: str):
    return [(ord(string[0]))-97,int(string[1])-1]

def cord_to_tile(list: list):
    return chr(list[0]+97)+str(list[1]+1)

def check_win(players: list):
    if (players[1].king == 0 or players[0].king == [2,4]):
        win('Black', players)
    if (players[0].king == 0 or players[1].king == [2,0]):
        win('White', players)

def pos_moves(players: list):
    for i in range(2):
        if players[i].turn == True:
            #for each card
            for card in range(len(players[i].deck)):
                #for each move
                for k in players[i].deck[card].moves:
                    #check king move
                    kingthere = cord_to_tile(((players[i].king[0] + players[i].direction*(k[0])), players[i].king[1] + players[i].direction*(k[1])))
                    checker = check_move(players[i],card,cord_to_tile(players[i].king), kingthere)
                    if checker == 0:
                        print(cord_to_tile(players[i].king) + ' ' + players[i].deck[card].name + ' ' + kingthere)
                    for l in range(len(players[i].pieces)):
                        piecethere = cord_to_tile((players[i].pieces[l][0] + players[i].direction * (k[0]), players[i].pieces[l][1] + players[i].direction * (k[1])))
                        checker = check_move(players[i],card,cord_to_tile(players[i].pieces[l]), piecethere)
                        if checker == 0:
                            print(cord_to_tile(players[i].pieces[l]) + ' ' + players[i].deck[card].name + ' ' + piecethere)

def check_move(player, card: int, where: str, there: str):
    #returns int based on type of failure, and 0 if succeded
    curcord = tile_to_cord(where)
    newcord = tile_to_cord(there)

    #checks if new position is in bounds
    if ((newcord[0]<0 or newcord[0]>4) or (newcord[1]<0 or newcord[1]>4)):
        return 1
    
    #checks if where is actually a piece
    checker = 0
    if player.king == curcord:
        checker = 1
    for piece in player.pieces:
        if (piece == curcord):
            checker = 1
    if (checker == 0):
        return 2
    
    #checks if a piece is already on there
    if player.king == newcord:
        return 3
    for piece in player.pieces:
        if (piece == newcord):
            return 3
        
    #checks if it is possible to move there with given card
    checker = 0
    for i in player.deck[card].moves:
        if (newcord == [(curcord[0]+(player.direction*i[0])),(curcord[1]+(player.direction*i[1]))]):
            checker = 1
    if (checker == 0):
        return 4
    
    #returns 0 when all tests passed
    return 0

def check_move_plus(player, card: int, where: str, there: str):
    checker = check_move(player, card, where, there)
    if checker == 0:
        return 1
    elif checker == 1:
        print("move out of bounds.\n")
    elif checker == 2:
        print("No movable piece at " + where + ".\n")
    elif checker == 3:
        print("Cannot move to " + there + ". One of your pieces is already there.\n")
    elif checker == 4:
        print("Impossible to move to " + there + " using " + player.deck[card].name + ".\n")
    return 0

def end_turn(players: list):
    board(players)
    for i in range(2):
        if players[i].turn == True:
            players[i].turn = False
        else:
            players[i].turn = True
            print("\n" + players[i].name + "'s turn")
    check_win(players)
    #test
    #print(players[0].turn,players[1].turn)

def move(players: list, where: str, there: str):
    #moves piece(where) to new position on board(there)
    curcord = tile_to_cord(where)
    newcord = tile_to_cord(there)
    for player in players:
        if (player.turn == True):
            if (player.king == curcord):
                player.king = newcord
                end_turn(players)
                return
            for i in range(len(player.pieces)):
                if (player.pieces[i] == curcord):
                    player.pieces[i] = newcord
                    end_turn(players)
                    return
                
def take(players: list, there: str):
    for i in range(len(players)):
        if players[i].king == tile_to_cord(there):
            players[i].king = 0
        for j in range(len(players[i].pieces)):
            if players[i].pieces[j] == tile_to_cord(there):
                players[i].pieces.pop(j)
                for k in range(2):
                    if players[k].turn == True:
                        print(players[k].name + " takes " + there + " piece.\n")
                        sleep(1)
                return
                
def movers_and_shakers(players: list, temp_deck: list, card: int, where: str, there: str):
    for i in range(2):
        if players[i].turn == True:
            if (check_move_plus(players[i], card, where, there) == 0):
                return
            temp_deck.append(players[i].deck.pop(card))
            players[i].deck.append(temp_deck.pop(0))
    take(players, there)
    move(players, where, there)