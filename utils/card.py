class Symbol:
    def __init__(self, color):
        self.color=color
        self.icon=['♥','♦', '♣', '♠']

class Card(Symbol):
    def __int__(self, value):
        self.value=['A', '2', '3', '4 ', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']