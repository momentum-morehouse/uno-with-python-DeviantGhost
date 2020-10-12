from random import randint

NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
COLORS = ["🔴","🟢","🟡","🔵"]
PLAYERS = []
PLAYER_REF = []
class Card:
    def __init__(self, number, color):
        self.number = number
        self.color = color

    def ___str___(self):
        return f"{self.color} {self.number}"   


class Player:
    def __init__(self, name, hand = []):

        self.name = name
        self.hand = hand
        PLAYERS.append(name)


class Deck:
    def __init__(self, numbers, colors):
        self.cards = []
        for number in numbers:
            for color in colors:
                card = (color, number)
                self.cards.append(card)

    def shuffle(self):
        shuffled_deck = []
        deck_to_shuffle = self.cards.copy()
        while len(deck_to_shuffle) > 0:
            card_to_move = deck_to_shuffle[randint(0, len(deck_to_shuffle)-1)]
            deck_to_shuffle.remove(card_to_move)
            shuffled_deck.append(card_to_move)
        return shuffled_deck


class Card_Pile:
    def __init__(self, card):
        self.card = card
    
    def __str__(self):
        return {self.card}


class Game:
    #Creates a shuffled deck
    def __init__(self):
        self.deck = Deck(NUMBERS, COLORS)
        self.shuffled_deck = self.deck.shuffle()
        
    #Gets a card from the top of the deck
    def getCard(self,deck):
        topCard = deck[0]
        deck.remove(deck[0])
        return topCard

    # def oneTurn(self,deck,hand,deck_Pile):
    #     print f"It is {PLAYERS[]}"


    def deal_start_hand(self, number_of_players,deck):
        for current_player in PLAYERS:
            temp_deck = deck
            while (len(PLAYER_REF[PLAYERS.index(current_player)].hand) < 7):
                PLAYER_REF[PLAYERS.index(current_player)].hand.append(temp_deck[0])
                deck.remove(temp_deck[0])    
        return temp_deck

def startGame():
    #Creates the game
    game = Game()

    #Gets deck
    deck = game.shuffled_deck
   
    #Creates the players with an empty hand
    enough_players = False
    while (enough_players == False):
        
        PLAYER_REF.append(Player(input(f"What is player {len(PLAYERS)+1}'s name: ")))
        
        if(len(PLAYERS) < 2):
            PLAYER_REF.append(Player(input(f"What is player {len(PLAYERS)+1}'s name: ")))
            
        more_players = input("Would you like to add more players? (y/n)")
        if (more_players == "n"):
            enough_players = True
    #Assigns starting hand to each player
    deck = game.deal_start_hand(len(PLAYERS),deck)
    print (PLAYER_REF[0].hand)
    print (PLAYER_REF[1].hand)

    #Starts the game of/Creates a card pile
    #card_Pile = Card_Pile(deck)
    
    #unoOut = False
    #While no one has one a player takes a turn
    # while (unoOut == False):
    #     card_Pile.card = oneTurn

startGame()
