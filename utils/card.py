class Symbol:
    def __init__(self, icon):
        if icon in ['♥', '♦', '♣', '♠']:
            self.icon = icon
        else:
            print('Invalid symbol')

        if self.icon == '♥' or self.icon == '♦':
            self.color = 'red'
        else:
            self.color = 'black'


class Card(Symbol):
    def __int__(self, value):
        if value in ['A', '2', '3', '4 ', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            self.value=value
        else:
            print('invalid value')