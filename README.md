# Six ship war
This is a miny game that programmed with python(used pygame module)

# Game Overview
In this game two players play against each other on a 5x5 board containing six
ships; three for each player. The goal is to get your ships across the board before the opponent.

# Set up
Player 1 has three ships at the beginning of the second, third and the fourth row, and
player 2 has three ships at the beginning of the second, third, and the fourth column.

# Turns
 At each turn, a player can move one of their ships. The ships can advance on their
existing row/column by one square. If one of opponent’s ships is located in front of one of our
ships, we can jump over that ship and advance by two squares, but if that square is also
occupied by an opposing ship, we can’t advance in that row/column, and must move another
ship.

# Free turn
If all of your opponents moves are restricted, their turn is lost and you get to play
again.

# Game Progression & Winning Condition
Each player moves one ship at their turn, until a player
has all of their ships placed on the opposite side of the board.
