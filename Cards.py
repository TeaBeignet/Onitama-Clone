#card objects
class Card():
    def __init__(self, name, player, moves):
        self.name = name
        self.player = player
        self.moves = moves
cards = []
cards.append(Card('Elephant', "Black", [(-1,0),(1,0),(-1,-1),(1,-1)]))
cards.append(Card('Ox', "White", [(0,1),(0,-1),(1,0)]))
cards.append(Card('Cobra',"Black",[(-1,0),(1,-1),(1,1)]))
cards.append(Card('Goose',"White",[(-1,-1),(-1,0),(1,0),(1,1)]))
cards.append(Card('Dragon',"Black",[(-2,-1),(2,-1),(-1,1),(1,1)]))
cards.append(Card('Rabbit',"White",[(1,-1),(2,0),(-1,1)]))
cards.append(Card('Rooster',"Black",[(-1,1),(-1,0),(1,0),(1,-1)]))
cards.append(Card('Tiger',"White",[(0,-2),(0,1)]))
cards.append(Card('Frog',"Black",[(-2,0),(-1,-1),(1,1)]))
cards.append(Card('Crane',"White",[(-1,1),(0,-1),(1,1)]))
cards.append(Card('Boar',"Black",[(-1,0),(0,-1),(1,0)]))
cards.append(Card('Crab',"White",[(-2,0),(0,-1),(2,0)]))
cards.append(Card('Horse',"Black",[(-1,0),(0,-1),(0,1)]))
cards.append(Card('Eel',"White",[(-1,-1),(-1,1),(1,0)]))
cards.append(Card('Mantis',"Black",[(-1,-1),(0,1),(1,-1)]))
cards.append(Card('Monkey',"White",[(-1,-1),(-1,1),(1,-1),(1,1)]))