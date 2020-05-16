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





