from random import shuffle
from copy import deepcopy
from .card import card
from .actions import get_card_list

class deck:
    def __init__(self):
        self.deck_list = self.load_deck()
        self.deck_copy = deepcopy(self.deck_list)
        self.size = len(self.deck_list)

    def __str__(self):
        return 'Число карт {}\nВ вашей руке: {}\nКарт на столе: {}'.format(
            len(self.deck_copy), len(self.deck_list) , [str(card) for card in self.deck_list]
        )

    def shuffle(self):
        shuffle(self.deck_list)

    def draw(self, number):

        if len(self.deck_list) < number:
            raise ValueError('Неосталось больше карт , '
                             'deck.refile() что бы играть сначала')
        drew = self.deck_list[:number]
        del self.deck_list[:number]

        self.size = len(self.deck_list)

        return drew

    def load_deck(self):
        card_list = []

    def refile(self):
        self.deck_list = deepcopy(self.deck_copy)
