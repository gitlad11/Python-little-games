from random import shuffle , randint
from copy import deepcopy

def get_card_list():

    values = ['2', '3', '4','5','6','7','8','9','10','J','Q','K','A']
    suits = ['Diamonds', 'Spades', 'Hearts', 'clubs']
    mounted_deck = []

    for _value in values:
        for _suit in suits:
            current_card = {}
            current_card['label'] = _value
            current_card['suit'] = _suit
            current_card['value'] = values.index(_value)

            mounted_deck.append(current_card)

        return mounted_deck

def get_label_value(label):
    _dict = {
        '2' : [2, 2],
        '3' : [3, 3],
        '4' : [4, 4],
        '5' : [5, 5],
        '6' : [6, 6],
        '7' : [7, 7],
        '8' : [8, 8],
        '9' : [9, 9],
        '10' : [10, 10],
        'J': [11, 11],
        'Q': [12, 12],
        'K': [13, 13],
        'A': [14, 1],
    }

    return _dict[label]

def poker_logic(hand_info,card_list):
    labels = hand_info['label_count']
    label_list = hand_info['labels']
    suits = hand_info['suit_count']
    suit_list = hand_info['suits']

    first_suit = suit_list[0]

    def high_card():
        game_value = 1
        return True , labels[label_list[-1]['content'], game_value]

    def pair():
        game_value = 2
        for key in labels:
            if labels[key]['count'] == 2:
                return True, labels[key]['content'], game_value

    def two_pairs():
        game_value = 3
        pairs = 0
        matched = []
        for key in labels:
            if labels[key]['count'] == 2:
                pairs += 1
                matched += labels[key]['content']

            if pairs == 2:
                return True,matched, game_value
            return False,[], game_value

    def three():
        game_value = 4
        for key in labels:
            if labels[key]['count'] == 3:
                return True , labels[key]['content'], game_value
            return False , [], game_value

    def straight():
        game_value = 5
        if len(label_list) < 5:
            return False , [] , game_value
        for label in label_list[1:]:
            if not get_label_value(label)[1] == get_label_value(label_list[label_list.index(label) - 1])[0] +1:
               return False, [], game_value
        return True , card_list , game_value

    def flash():
        game_value = 6
        if suit_list == [first_suit]:
            return True, card_list , game_value
        return False, [], game_value

    def full_house():
        game_value = 7
        three = False
        pairs = False
        for key in labels:
            if labels[key]['count'] == 3:
                three = True
            if labels[key]['count'] == 2:
                pairs = True

        if three and pair:
            return True, card_list , game_value
        return False, [], game_value

    def four():
        game_value = 8
        for key in labels:
            if labels[key]['count'] == 4:
                return True, labels[key]['content'], game_value
        return False , [], game_value

    def street_flash():
        game_value = 9
        if len(label_list) < 5:
            return False, [], game_value
        for label in label_list[1:]:
            if not get_label_value(label)[1] == get_label_value(label_list[label_list.index(label) - 1])[0] + 1:
                return False, [], game_value

        if not suit_list == [first_suit]:
            return False, [], game_value

        return True, card_list, game_value

    def royal_street_flash():
        game_value = 10
        if not suit_list == [first_suit]:
            return False, [], game_value

        if not label_list == ['10', 'J', 'Q', 'K', 'A']:
            return False, [], game_value

        return True, card_list, game_value


    combinations = [
        high_card(),
        pair(),
        two_pairs(),
        three(),
        straight(),
        flash(),
        full_house(),
        four(),
        street_flash(),
        royal_street_flash(),
    ]

    for comb in combinations:
        if comb[0]:
            return comb

def get_comb_name(value):

    combinations ={
        1 : 'старшая карта',
        2 : 'пара',
        3 : 'две пары',
        4 : 'три подряд',
        5 : 'стрит',
        6 : 'флэш',
        7 : 'фул хаус',
        8 : 'каре',
        9 : 'стрит флэш',
        10 : 'флэш рояль',
    }

def compare_games(table):

    _sorted = []
    count = 0
    while count < len(table):
        winner_index = count
        winner_obj = table[winner_index]
        winner_hand = winner_obj.hand
        for player in table[count:]:
            h = player.hand
            if h.game_value == winner_hand.game_value:
                for h_card in h.comb_labels_list :
                    h_values = get_label_value(h_card)[0]
                for w_card in winner_hand.comb_labels_list :
                    w_values = get_label_value(w_card)[0]

                    if sum(h_values) > sum(w_values):
                        winner_index = table.index(player)
                        winner_obj = player
                        winner_hand = winner_obj.hand
                    elif sum(h_values) == sum(w_values):
                        if player != winner_obj:
                            player.splitted = True
                            winner_obj.splitted = True

                    elif h.game_value > winner_hand.game_value:
                        winner_index = table.index(player)
                        winner_obj = player
                        winner_hand = winner_obj.hand

                    _sorted.append(winner_obj)
                    count - len(_sorted)

                return _sorted

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


class deck:
    def __init__(self):
        #self.deck_list = self.load_deck()
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

class hand:

    def __init__(self, cards):
        self.cards = cards
        self.sort()
        self.labels, self.labels_list , self.suits, self.suits_list = self.hand_values()
        self.hand_info = {
            'label_count' : self.labels,
            'labels' : self.labels_list,
            'suit_count' : self.suits,
            'suit' : self.suits_list
        }
        self.game_raw = poker_logic(self.hand_info, self.cards)
        self.game_value = self.game_raw[2]
        self.game_cards_raw = self.game_raw[1]
        self.game_cards = [str(card) for card in self.game_raw[1]]
        self.game_name = get_comb_name(self.game_raw[2])
        self.game = self.mount_game()

        self.game_labels, self.game_labels_list, self.game_suits, self.game_suits_list = self.hand_values(
            self.game_cards_raw)
        self.game_info = {
            'label_count': self.game_labels,
            'labels': self.game_labels_list,
            'suit_count': self.game_suits,
            'suits': self.game_suits
        }

    def __str__(self):
        return str([str(card) for card in self.cards])

    def get_info(self):
        return 'Hand: \t{}\nInfo: \t{}'.format(str([str(card) for card in self.cards]), self.hand_info)

    def mount_game(self):
        return '{} - {}'.format(self.game_name, self.game_cards)

    def hand_values(self, target_list=None):

        labels = {}
        labels_list = []
        suits = {}
        suits_list = []

        if not target_list:
            target_list = self.cards

        for card in target_list:
            if not labels.get(card.label):
                labels[card.label] = {'count': 1, 'content': [card]}
                labels_list.append(card.label)
            else:
                labels[card.label]['count'] += 1
                labels[card.label]['content'].append(card)

            if not suits.get(card.suit):
                suits[card.suit] = {'count': 1, 'content': [card]}
                suits_list.append(card.suit)
            else:
                suits[card.suit]['count'] += 1
                suits[card.suit]['content'].append(card)

        return labels, labels_list, suits, suits_list

    def sort(self):

        count = 0
        lower_index = 0

        while count < len(self.cards):
            lower_index = count
            low_card = self.cards[lower_index]
            for card in self.cards[count:]:
                if card.value < low_card.value:
                    lower_index = self.cards.index(card)
                    low_card = self.cards[lower_index]

            dummy = low_card
            self.cards[lower_index] = self.cards[count]
            self.cards[count] = dummy
            count += 1


my_deck = deck()
my_deck.shuffle()

def start_game(players):
    table = []
    for count in range(players):
        player = player(hand(my_deck.draw(5)))
        table.append(player)

        print(player , player.hand.game_cards)

    table = compare_games(table)

    winner = table[0]
    if winner.splitted:
        winner_table = splitted_pot(table)
        print('\n Выигрыш поделен между')
        print('победителями')
        for player in winner_table:
            print('игроки: {} - {} - {} '.format(player.name, player.hand.game_name , player.hand.game_cards))
    else:
        print('\n Победитель: {} - {} - {}'.format(winner.name, winner.hand.game_name, winner.hand.game_cards))

def splitted_pot(table):
    winner_table = []
    for player in table:
        if player.splitted ==True:
            if player not in winner_table:
                winner_table.append(player)
        else:
            break
        return winner_table

start_game(4)