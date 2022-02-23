from player import Player
from player import Deck

class Board:

    def start_game(self):
        print("Hey hey hey!! welcome to my cool card game!! how many players would you like to play with??")
        new_deck=Deck(int(input()))
        new_deck.fill_deck()
        new_deck.shuffle()
        new_deck.player_profile()
        new_deck.distribute()
        new_deck.play()

        print("Thank you so much for playing my game!! Hope you enjoyed it and hope to see you soon! Ciao!")











