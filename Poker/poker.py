from .hand import hand
from .players import player
from .deck import deck
from .actions import compare_games

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