class Player():
    def __init__(self, deck, name, turn, king, pieces, direction):
        self.deck = deck
        self.name = name
        self.turn = turn
        self.king = king
        self.pieces = pieces
        self.direction = direction

black = Player([],"Black",False,[2,0],[[0,0],[1,0],[3,0],[4,0]],-1)
white = Player([],"White",False,[2,4],[[0,4],[1,4],[3,4],[4,4]],1)
players = [black,white]