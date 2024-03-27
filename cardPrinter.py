def print_card(card):
    suit = card['suit']
    card_name = card['card_face']

    suit_symbol_dict = {
        "Hearts": '♥',
        "Diamonds": '♦',
        "Clubs": '♣',
        "Spades": '♠'
    }

    suit_icon = suit_symbol_dict[suit]

    print('┌───────────────┐')
    print(f'|      {card_name:<2}       |')
    print('|               |')
    print('|               |')
    print('|               |')
    print(f'|       {suit_icon:<2}      |')
    print('|               |')
    print('|               |')
    print('|               |')
    print('|               |')
    print(f'|     {card_name:>2}        |')
    print('└───────────────┘')


# Example usage:

# TODO: print denomination X suit-icon