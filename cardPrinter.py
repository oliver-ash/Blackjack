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
    print(f'|      {card_name:<2}       | ')
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

# Print hand
# All card information must be gathered before printing hand (bc line by line printing)
# Information can be stored in lists (ie. suits, number)

def print_hand(hand):

    suit_symbol_dict = {
        "Hearts": '♥',
        "Diamonds": '♦',
        "Clubs": '♣',
        "Spades": '♠'
    }
 
    n = len(hand)
    print('┌───────────────┐ ' * n)
    for card in hand:
        card_name = card['card_face']
        print(f'|      {card_name[0]:<2}       |', end = ' ')
    print('')
    print('|               | ' * n)
    print('|               | ' * n)
    print('|               | ' * n)
    for card in hand:
        suit = card['suit']
        suit_icon = suit_symbol_dict[suit]
        print(f'|      {suit_icon:<2}       |', end = ' ')
    print('')
    print('|               | ' * n)
    print('|               | ' * n)
    print('|               | ' * n)
    for card in hand:
        card_name = card['card_face']
        print(f'|      {card_name[0]:<2}       |', end = ' ')
    print('')
    print('└───────────────┘ ' * n) 
    