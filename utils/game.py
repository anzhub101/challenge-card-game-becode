from player import Deck

class Board:
    def __init__(self, players, turn_count, active_cards, history_cards):
        self.players=Player[]
        self.turn_count=turn_count
        self.active_cards=Player.history[Player.history.len()-1]
        self.history_cards=Player.history[:Player.history.len()-2]

    def start_game(self):
        new_deck=Deck()
        new_deck.fill_deck()
        new_deck.distribute()
        i=0
        for crds in Player[i].cards:
            Player[i].play()
            print(f'the turn count is ({Player[i].turn_count}' )
            i+=1
            Player[i].turn_count+=1
            print(f'The active cards are {Player.card} and all the cards played in the past are {Player.history}')








