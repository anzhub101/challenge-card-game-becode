from player import Player
from player import Deck

class Board:
    def __init__(self, players, active_cards, history_cards):
        self.players=players
        self.turn_count=[]
        self.active_cards=active_cards
        self.history_cards=history_cards

    def start_game(self):
        print("Hey hey hey!! welcome to my cool card game!! how many players would you like to play with??")
        new_deck=Deck(int(input()))
        new_deck.fill_deck()
        new_deck.shuffle()
        new_deck.player_profile()
        new_deck.distribute()

            print(f'the turn count is ({.turn_count[i]}' )
            turn_count[i]+=1
        i+=1
            print(f'The active cards are {} and all the cards played in the past are {}')








