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

def print_hand(hand, height = 2, width = 4): # Height is rows between each symbolic row, width is half of spaces to right of face symbol line on first line

    suit_symbol_dict = {
        "Hearts": '♥',
        "Diamonds": '♦',
        "Clubs": '♣',
        "Spades": '♠'
    }
 
    n = len(hand)
    print(('┌───'+ width*2 * '─' + '┐ ') * n)
    for card in hand:
        if 'is_hidden' in card and card['is_hidden'] == True:
            card_name = '?'
        elif card['card_face'] == '10':
            card_name = card['card_face']
        else:
            card_name = card['card_face'][0]
        print(f'| {card_name:<2}' + width*2 * ' ' + '|', end = ' ')
    print('')
    height_counter = 0
    while height_counter < height:
        print(('|   ' + width*2 * ' ' + '| ') * n)
        height_counter += 1
    for card in hand:
        if 'is_hidden' in card and card['is_hidden'] == True:
            suit_icon = '?'
        else:
            suit = card['suit']
            suit_icon = suit_symbol_dict[suit]
        print(f'|' + width * ' ' +f' {suit_icon:<2}' + width * ' ' + '|', end = ' ')
    print('')
    height_counter = 0
    while height_counter < height:
        print(('|   ' + width*2 * ' ' + '| ') * n)
        height_counter += 1
    for card in hand:
        if 'is_hidden' in card and card['is_hidden'] == True:
            card_name = '?'
        elif card['card_face'] == '10':
            card_name = card['card_face']
        else:
            card_name = card['card_face'][0]
        print('| ' + width*2 * ' ' + f'{card_name:<2}|', end = ' ')
    print('')
    print(('└───' + width*2 * '─' + '┘ ') * n) 
    