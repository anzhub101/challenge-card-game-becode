from card import Card
import random


class Deck:

    def __init__(self, no_of_players, players_name):
        self.card_symb = ['♥', '♦', '♣', '♠']
        self.card_num = ['A', '2', '3', '4 ', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = []
        self.player_hands = []
        self.no_of_players = no_of_players
        self.player_list = []
        self.players_name = players_name
        self.hands=[]

    def fill_deck(self):
        for i in self.card_symb:
            for j in self.card_num:
                self.cards.append([i, j])

    def shuffle(self):
        random.shuffle(self.cards)

    def distribute(self):
        if self.no_of_players/2==0:
            cards_per_person=52/self.no_of_players
            j = 0
            for i in range(0,51):
                for i in range(0, cards_per_person - 1):
                    self.player_hands.append(self.cards[i][j])
                    j += 1
                self.hands.append(self.player_hands)
        else:
            remainder=52%self.no_of_players
            print(f'Since you are an odd no. of players, the first {remainder} of you will get an extra card')
            cards_per_person = 52 / self.no_of_players
            cards_per_person=int(cards_per_person)
            j = 0
            for i in range(0, 51-remainder):
                for i in range(0, cards_per_person - 1):
                    self.player_hands.append(self.cards[i][j])
                    j += 1
                self.hands.append(self.player_hands)
            j = 0
            for i in range(51-remainder, 51):
                self.player_hands[j].append(self.cards[i][i])
                j+=1


    def player_profile(self):
        for i in self.no_of_players:
            input(self.players_name)
            self.player_list.append(self.players_name)

class Player(Deck):

    def __int__(self, card, turn_count, number_of_cards, history, player_name):

        self.card = hands
        self.turn_count = int(turn_count)
        self.number_of_cards = int(number_of_cards)
        self.player_name = Deck.players_name
        self.history = []

    def play(self):
        rand_card = self.card[random.randint(0, len(self.card))]
        self.history.append(rand_card)
        self.card.remove(rand_card)
        print(f'{self.player_name} {self.turn_count} played:{rand_card}')

        return rand_card
