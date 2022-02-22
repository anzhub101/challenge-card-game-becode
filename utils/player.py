from card import Card

import random

class Player:
    def __int__(self,card,turn_count,number_of_cards,history,player_name):
        self.card=Card()
        self.turn_count=int(turn_count)
        self.number_of_cards=int(number_of_cards)
        self.player_name=player_name
        self.history=Card()

    def play(self):
        rand_card= self.card[random.randint(0,len(self.card))]
        self.history.append(rand_card)
        self.card.remove(rand_card)
        print(f'{self.player_name} {self.turn_count} played:{rand_card}{Card.value}')

        return rand_card

class Deck(Player):
    def __del__(self, cards):
        self.cards=Card[[]]

    def fill_deck(self):
        for i in Card.icon.len():
            for j in Card.value.len():
                self.cards.append([Card.icon[i],Card.value[j],'red'])
                self.cards.append([Card.icon[i],Card.value[j],'black'])

    def shuffle(self):
        random.shuffle(self.cards)

    def distribute(self):
        no_of_players=Player[]
        j=0
        for i in no_of_players:
            no_of_players[i].card.append(self.cards[i][j])
            j+=1
































