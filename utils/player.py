import random


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

    def fill_deck(self):
        for i in self.card_symb:
            for j in self.card_num:
                self.cards.append([i, j])

    def shuffle(self):
        random.shuffle(self.cards)

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

    def player_profile(self):
        print("Now enter enter the names of the players you want to play with. Make sure to enter an equal "
              "number of names to the number of players you wanted to play with, if not you are a liar and this game doesnt work for liars!")
        for i in self.no_of_players:
            input(self.players_name)
            self.player_list.append(self.players_name)


class Player(Deck):

    def __int__(self):

        self.card = []
        self.turn_count = 0
        self.number_of_cards = 0
        self.player_name = ''
        self.history = []
        Deck.__init__(self, no_of_players)

    def play(self):
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

#figure out the turn count