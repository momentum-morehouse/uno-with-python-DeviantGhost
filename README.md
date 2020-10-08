# UNO Game with Python

### You will be creating a modified UNO game using Python, starting with the notes and code from class.
### Start with the uno.py file we created in class, and move it into this directory using the command line, finder, or file explorer.

## Version 1.0
- 2 players
- No action cards
- Player wins when they run out of cards

## Version 2.0
- Add action cards one at a time

Notes from class: 

#### Number cards 0-9
#### 4 Colors 
- Red
- Green
- Yellow
- Blue

#### Version 2.0
#### Action cards 
- Reverse
- Draw 2
- Draw 4
- Wild
- Wild Draw 4
- Skip

#### Start 
- Dealer deals 7 cards to each player
- Deck set aside
- Pull one random card from the deck and put it face up

#### Turns
- If player has card that matches color or number, place on top of deck.
- If no matching card, draw one from the deck. If you can play that card, you do.
- Turn moves on to next person. 

#### Winner
- When one player runs out of cards.
- You have to say "UNO" when you have one card left.

Version 1.0
#### Classes:
#### Card
    - Number
    - Color

#### Deck
    - Made up of cards
    - No cards can be missing
    - Able to be shuffled
    - Able to be drawn from

#### Player
    - Name
    - Hand
    - Contains cards
    - Starting number of cards
    - Able to Draw from the deck
    - Able to throw out cards
    - Able to win or lose

#### Game
    - Players
    - Rounds
    - Each player takes a turn
