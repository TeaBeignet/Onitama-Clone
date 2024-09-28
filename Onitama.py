import random
from Move import*
#from Printer import*
from Cards import*
from Players import*

def draw():
    #draws cards to decks and determines order of play
    for _ in range(2):
        players[0].deck.append(cards.pop(random.randint(0, len(cards)-1)))
        players[1].deck.append(cards.pop(random.randint(0, len(cards)-1)))
    temp_deck = [cards.pop(random.randint(0, len(cards)-1))]
    if (temp_deck[0].player == "Black"):
        players[0].turn = True
        print("Black begins\n")
        sleep(1)
    else:
        players[1].turn = True
        print("White begins\n")
        sleep(1)
    return temp_deck

def Listen(cmd: str, players, temp_deck):
    cmd = cmd.split()

    #/deck command
    if cmd[0].lower() == '/deck':
        if (len(cmd)<2):
            print("Too few arguments, try again.")
            return
        
        if cmd[1].lower() == 'black':
            print_deck(players[0].name,players[0].deck,players[0].direction)
        elif cmd[1].lower() == 'white':
            print_deck(players[1].name,players[1].deck,players[1].direction)
        elif cmd[1].lower() == "the people's" or cmd[1].lower() == 'temp':
            for i in range(2):
                if players[i].turn == True:
                    print_deck('The people', temp_deck, players[i].direction)

        else:
            print(cmd[1] + " not a known deck. Please enter 'white', 'black', or 'temp' / 'the people's'.")

    #/board command
    elif cmd[0].lower() == '/board':
        board(players)

    #/pmoves command
    elif cmd[0].lower() == '/possiblemoves' or cmd[0].lower() == '/pmoves':
        pos_moves(players)

    #/move command
    elif cmd[0].lower() == '/move':
        if (len(cmd)<4):
            print("Too few arguments, try again.")
            return
        
        checker = 0
        for i in range(2):
            if players[i].turn == True:
                for j in range(2):
                    if players[i].deck[j].name.lower() == cmd[2].lower():
                        card = j
                        checker = 1
            else:
                print("No such card: "+cmd[2]+"\n")
        if checker == 1:
            movers_and_shakers(players, temp_deck, card, cmd[1], cmd[3])

    #/help command
    elif cmd[0].lower() == '/help' or cmd[0] == '/?':
        print("'/help' or '/?'\n\n'/rules'\n\n'/board'\n\n'/deck' followed by 'white', 'black', or 'temp'\n\n'/pmoves' or '/possiblemoves'\n\n'/move' followed by the tile coordinates of the piece you want to move, the name of the card you want to use to move the piece, and the tile coordinates you want to move the piece to.\n")

    #/rules command
    elif cmd[0].lower() == '/rules':
        board(players)
        x = 3
        print("This is the board. As you can see, each team has 5 pieces.\n")
        sleep(x)
        print("Let's say you were playing 'white'(♚ ). Which is only really white if you're using darkmode.\n")
        sleep(x)
        print("(If you want to change that swap line 39 in printer with line 43, and line 45 with line 47.)\n")
        sleep(x)
        print("Let's take a look at your deck using the '/deck white' command.")
        sleep(x)
        print_deck('White', players[1].deck, players[1].direction)
        print("\nThe □  box represents where your piece is currently.\nThe ▣  box represents where you can move relative to □.\n")
        sleep(x)
        print_card(Card('Frog',"Black",[(-2,0),(-1,-1),(1,1)]),1)
        print("\nThis is what the Frog card would look like in the 'white'(♚ ) deck.\n")
        sleep(x)
        print_card(Card('Frog',"Black",[(-2,0),(-1,-1),(1,1)]),-1)
        print("\nThis is what the same card will look like when it is in the 'black'(♔ ) deck.\nThis is because they would view the board from the opposite angle.")
        sleep(x)
        Listen("/deck temp",players,temp_deck)
        print("\nThis is the 'temp' deck, or 'The people's' deck. It is shown from the perspective of the player whose turn it is.\nOnce your turn ends, the card you used will enter the temp deck, and the card in the temp deck will go to your deck.\n")
        sleep(x)
        print("Anytime you want to make a move you will use the /move command.\nLet's take a look at the possible moves you could make using '/pmoves'.\n")
        sleep(x)
        Listen("/pmoves",players,temp_deck)
        sleep(x)
        print("\nTo move you can use the format:\n /move [current piece position] [card to use] [new piece position]\n")
        sleep(x)
        print("You can win in two ways.\nEither capture the opposing king, or move your king to the starting position of your opponent's king.\n")
        sleep(x)
        print("Good luck! Have fun. O‿O")

    #default
    else:
        print(cmd[0] + " is an unrecognized command. Enter '/?' or '/help' to view a list of acceptable commands.")
    # print(cmd)

def onitama(players):
    temp_deck = draw()
    print_deck(players[0].name, players[0].deck, players[0].direction)
    print_deck(players[1].name, players[1].deck, players[1].direction)
    print_deck("The people",temp_deck,1)
    print("\n")
    board(players)
    while True:
        cmd = input("")
        if cmd[0] == '/':
            Listen(cmd, players, temp_deck)

#run
onitama(players)

#testing setup to match fail case in changelog
# temp_deck = [cards[1]]
# players[1].turn = True
# players[0].deck = [cards[8], cards[7]]
# players[1].deck = [cards[15], cards[11]]
# #running test
# print_deck(players[0].name, players[0].deck, players[0].direction)
# print_deck(players[1].name, players[1].deck, players[1].direction)
# print_deck("The people",temp_deck,1)
# board(players)
# while True:
#     cmd = input("")
#     if cmd[0] == '/':
#         Listen(cmd, players, temp_deck)