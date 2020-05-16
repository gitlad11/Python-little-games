from random import shuffle , randint

class player:
    def __init__(self, hand , name=None):

        self.hand = hand
        if not name:
            self.hame = self.get_input_name()
        else:
            self.name = name
        self.splitted = False

    def __str__(self):
        return '{}: партия: {}'.format(self.name, self.hand.comb_name)

    def get_input_name(self):
        with open('names.txt', 'r') as file:
            data = file.readlines()
        return input()





