import random

"""Although as per the instructions it is not supposed to be this way, this had over the course of making the project 
become the main class in this file. The class Player below inherits this classIn this class, we have 4 methods and the 
appropriate attributes of the class. A lot of new attributes were added, although they werent meant to be; as per the 
instruction. But some of the previous changes made in this program have been committed so i beleive although, not the 
whole course of action, but some of the changes can be seen, and hopefully it might be possibel to understand why 
the player file has become like this"""

class Deck:

    def __init__(self, no_of_players):
        self.card_symb = ['♥', '♦', '♣', '♠']
        self.card_num = ['A', '2', '3', '4 ', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = []
        self.player_hands = []
        self.no_of_players = no_of_players
        self.player_list = []
        self.players_name = ''
        self.hands = []

    """ The below method creates a deck every time a game is played. Although it is possible to create the deck using 
    the classes in card.py for simplicity purposes"""
    def fill_deck(self):
        for i in self.card_symb:
            for j in self.card_num:
                self.cards.append([i, j])

    """The below method is used to simply randomly shuffle the cards once a standard deck is created"""

    def shuffle(self):
        random.shuffle(self.cards)

        """the logic behind the below function distribute is that all the players get a fair number of cards and there 
        are no limitations on the number of players that can play the game.
        The first if/else statement checks whether the players can get n equal or unequal number of cards. 
        After checking it assigns the cards to the players equally. Here there isnt any list of players created, but rather 
        the cards are assigned to a list which has equal indexing to the number of players playing. Hence calling the index
        from a player list should correspond to that from the cards list. 
        """

    def distribute(self):
        if 52 % self.no_of_players == 0:
            cards_per_person = 52/self.no_of_players
            x=0
            for i in range(0, self.no_of_players-1):
                for j in range(x, x + cards_per_person - 1):
                    self.player_hands.append(self.cards[j])
                self.hands.append(self.player_hands)
                x+=cards_per_person
        else:
            remainder = 52 % self.no_of_players
            print(f'Since you are an odd no. of players, the first {remainder} of you will get an extra card')
            cards_per_person = 52 / self.no_of_players
            cards_per_person = int(cards_per_person)
            x = 0
            for i in range(0, self.no_of_players - 1):
                for j in range(x, x + cards_per_person - 1):
                    self.player_hands.append(self.cards[j])
                self.hands.append(self.player_hands)
                x += cards_per_person
            j = 0
            for i in range(51-remainder, 51):
                self.player_hands[j].append(self.cards[i])
                j += 1

    """The below method is used to create a list of all the players that the user wants to enter"""

    def player_profile(self):
        print("Now enter enter the names of the players you want to play with. Make sure to enter an equal number of "
              "names to the number of players you wanted to play with, if not you are a liar and this game doesnt work for liars!")
        for i in self.no_of_players:
            input(self.players_name)
            self.player_list.append(self.players_name)


"""This was supposed to be the main class, and although the instructions had requested to pass certain attributes for 
initialization, in the end it hadnt been done. The class contains quite a few attributes and one method. The method will 
be explained in detail below"""

class Player(Deck):

    def __int__(self):

        self.card = []
        self.turn_count = 0
        self.number_of_cards = 0
        self.player_name = ''
        self.history = []

    """The method below is the main method that runs the game. In this method all the turns of all the players are 
    played and a list, including the name, history of cards and turns played are also created in order to keep track.The
    method heavily depends on the class Deck and its attributes and methods, and needs it in order to run properly. The 
    below method works by attaining a player from the list of players created in the previous class, and assigning them 
    with a hand. after assigning them with a hand, a random card from the hand is played and then deleted from active 
    cards. The same card is added to a list with all played cards per player. The method is looped and plays all the 
    cards of all teh players one after the other"""

    def play(self):
        Deck.__init__(self)
        rand_card = []
        List_of_players = []
        j = 0
        for i in self.hands:
            self.player_name = self.player_list[j]
            self.card = i
            for cards in self.card:
                rand_card = self.card[random.randint(0, len(self.card))]
                self.history.append(rand_card)
                self.card.remove(rand_card)
                print(f'{self.player_name} is playing his {self.turn_count} turn. His active cards are {self.card} and the card he played is:{rand_card}/n'
                      f'These are the cards he has left to play {len(self.history)}')
                self.turn_count += 1
            a= [self.player_name, self.turn_count, self.history, self.number_of_cards]
            List_of_players.append(a)
            j+=1

        return rand_card
