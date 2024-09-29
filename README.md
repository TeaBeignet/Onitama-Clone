# Onitama-Clone
This is a python exercise I did over the course of 5 days. It is a playable text based version of the boardgame 'Onitama.'

Run Onitama.py to begin.



Use the following commands to play the game (visible through use of /help or /? commands):

'/help' or '/?'

'/rules'

'/board'

'/deck' followed by 'white', 'black', or 'temp'

'/pmoves' or '/possiblemoves'

'/move' followed by the tile coordinates of the piece you want to move, the name of the card you want to use to move the piece, and the tile coordinates you want to move the piece to.



Here is an example introduction to the rules and functionality of the game(visible through /rules command):

        1|[♙][♙][♔][♙][♙]|
        2|[-][-][-][-][-]|
        3|[-][-][-][-][-]|
        4|[-][-][-][-][-]|
        5|[♟][♟][♚][♟][♟]|
           a  b  c  d  e
This is the board. As you can see, each team has 5 pieces.

Let's say you were playing 'white'(♚). Which is only really white if you're using darkmode.

(If you want to change that swap line 39 in printer with line 43, and line 45 with line 47.)

Let's take a look at your deck using the '/deck white' command.

White's Deck:
Name: The Dragon
        □ □ □ □ □
        ▣ □ □ □ ▣
        □ □ ■ □ □
        □ ▣ □ ▣ □
        □ □ □ □ □
Name: The Frog
        □ □ □ □ □
        □ ▣ □ □ □
        ▣ □ ■ □ □
        □ □ □ ▣ □
        □ □ □ □ □

The □  box represents where your piece is currently.
The ▣  box represents where you can move relative to □.

Name: The Frog
        □ □ □ □ □
        □ ▣ □ □ □
        ▣ □ ■ □ □
        □ □ □ ▣ □
        □ □ □ □ □

This is what the Frog card would look like in the 'white'(♚ ) deck.

Name: The Frog
        □ □ □ □ □
        □ ▣ □ □ □
        □ □ ■ □ ▣
        □ □ □ ▣ □
        □ □ □ □ □

This is what the same card will look like when it is in the 'black'(♔ ) deck.
This is because they would view the board from the opposite angle.

The people's Deck:
Name: The Elephant
        □ □ □ □ □
        □ □ □ □ □
        □ ▣ ■ ▣ □
        □ ▣ □ ▣ □
        □ □ □ □ □

This is the 'temp' deck, or 'The people's' deck. It is shown from the perspective of the player whose turn it is.
Once your turn ends, the card you used will enter the temp deck, and the card in the temp deck will go to your deck.

Anytime you want to make a move you will use the /move command.
Let's take a look at the possible moves you could make using '/pmoves'.

c1 Crab c2
a1 Crab a2
b1 Crab b2
d1 Crab d2
e1 Crab e2
c1 Eel d2
a1 Eel b2
b1 Eel c2
d1 Eel e2

To move you can use the format:
 /move [current piece position] [card to use] [new piece position]

You can win in two ways.
Either capture the opposing king, or move your king to the starting position of your opponent's king.

Good luck! Have fun. O‿O
