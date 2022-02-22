from card import Card
import random


class Player:

    def __int__(self, card, turn_count, number_of_cards, history, player_name):
        self.card_list = []
        self.history_list = []
        self.card = Card()
        self.card_list.append(self.card)
        self.turn_count = int(turn_count)
        self.number_of_cards = int(number_of_cards)
        self.player_name = player_name
        self.history = Card()
        self.history_list.append(self.history)

    def play(self):
        rand_card = self.card_list[random.randint(0, len(self.card_list))]
        self.history_list.append(rand_card)
        self.card_list.remove(rand_card)
        print(f'{self.player_name} {self.turn_count} played:{rand_card}{Card.value}')

        return rand_card


class Deck(Player):

    def __init__(self):
        self.card_symb = ['♥', '♦', '♣', '♠']
        self.card_num = ['A', '2', '3', '4 ', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = []
        self.sample_card = Card()

    def fill_deck(self):
        for i in self.card_symb:
            for j in self.card_num:
                self.cards.append([i, j])

    def shuffle(self):
        random.shuffle(self.cards)

    def distribute(self, no_of_players):
        self.no_of_players = no_of_players
        j = 0
        for i in no_of_players:
            no_of_players[i].card.append(self.cards[i][j])
            j += 1
