def print_card(suit, card_name):
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
print_card('Spades', '2')

# TODO: print denomination X suit-icon