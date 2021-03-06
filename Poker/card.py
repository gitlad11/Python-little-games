class card:

    def __init__(self, label , suit, value):

        self.label = label
        self.suit = suit
        self.value = value
        self.suit_symbol = self.get_suit_symbol()
        self.abr_suit = self.suit_shorter()

    def __str__(self):
        return '{}{}'.format(self.label, self.suit_symbol)

    def suit_shorter(self):
        return self.suit[0].upper()

    def get_suit_symbol(self):
        symbols = {
            'Hearts': '♥',
            'Diamonds': '♦',
            'Clubs': '♣',
            'Spades': '♠'
        }
        return symbols[self.suit]
