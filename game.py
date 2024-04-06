import requests
import sys

from cardPrinter import print_card
from cardPrinter import print_hand

# Create a list of dictionaries for deck 2-14 each suit
denom_dict = {
'2': '2',
'3': '3',
'4': '4', 
'5': '5',
'6': '6', 
'7': '7', 
'8': '8',
'9':'9',
'10':'10',
'11': 'Ace',
'12': 'Jack',
'13': 'Queen',
'14': 'King'
}

def get_value_from_denomination(denomination):
    if denomination > 11:
        return 10
    return denomination

def generate_true_random(a, b):
    source = f"https://www.random.org/integers/?num=1&min={a}&max={b}&col=5&base=10&format=plain&rnd=new"
    number = requests.get(source)
    number = int(number.text)
    return number


def create_playing_deck(n=1): # n = number of decks
    # Create 4 suits with number values 2-14 and ace, jack, queen king
    '''
    sample_card =  {
        'suit': 'Spade', 
        'card_face': 'Ace'
        'value': 11
    }
    If denom is greater than 11 it's value is 10
    '''
    # n x 13 = suit totals: how many cards of a given suit
    # list of suits
    # List of denominations
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    denominations = list(range(2, 15))
    deck = []

    # 
    for suit in suits: 
        for denomination in denominations:
            
            card = {
                'suit': suit,
                'card_face': denom_dict[str(denomination)],
                'value': get_value_from_denomination(denomination)
            }
            deck.append(card)
    return deck

def draw_card_from_deck(deck):
    # Generate a truly random number
    # Remove card from the deck, deck is mutated (if deck is printed line after, deck is changed)
    card = deck.pop(generate_true_random(1, len(deck)-1))
    return card

# new_deck = create_playing_deck()

# new_card = draw_card_from_deck(new_deck)
# print(new_card)

# if new_card in new_deck:
#     print('Card not deleted')
# else:
#     print('Card deleted')


def setup():
    initial_input = input('Type 1 to start game. Type any other character to exit. ')
    print(int(initial_input) == 1)
    if int(initial_input) == 1:
        play_game()
    else:
        sys.exit(0)

def determine_outcome(deck, your_hand, dealer_hand, dealer_points, your_points):
    # If dealer's total 16 or below, must hit
    if dealer_points <= 16:
        dealer_hand.append(draw_card_from_deck(deck))
        dealer_points = totaler(dealer_hand)

    # If dealer's total 17 or over, must stand

    # If anyone goes over 21, they bust
    if dealer_points > 21 and your_points > 21:
        print('Tie!')
    elif dealer_points > 21:
        print('Dealer busts!')
    elif your_points > 21:
        print('You bust!')
    elif your_points > dealer_points:
        print('You win!')
    elif dealer_points > your_points:
        print('Dealer wins!')
    show_table(your_hand, dealer_hand)
    print('Final_points: ','Your points: ', your_points, 'Dealer points: ', dealer_points)

    #_point X >_point Y = X wins

def totaler(hand):
    points = 0
    for card in hand:
        points += card['value']
    return points

def deal_card_to_player(hand, deck, hidden=False):
    if hidden == False:
        hand.append(draw_card_from_deck(deck))
    else:
        hidden_card = draw_card_from_deck(deck)
        hidden_card['is_hidden'] = True
        hand.append(hidden_card)

def initial_deal(deck, dealer_hand, your_hand):
    deal_card_to_player(dealer_hand, deck, hidden=True)
    deal_card_to_player(dealer_hand, deck, hidden=False)

    deal_card_to_player(your_hand, deck)
    deal_card_to_player(your_hand, deck)

def show_table(your_hand, dealer_hand):
    print('Your hand: ')
    print_hand(your_hand)
    print('Dealer hand: ')
    print_hand(dealer_hand)


def play_game():
    game_running = True
    deck = create_playing_deck()
    dealer_hand = []
    your_hand = []
    dealer_points = 0
    your_points = 0
    
    while game_running == True:
        print("I'm playing the game!")
        print('Dealer deals cards: ')
        initial_deal(deck, dealer_hand, your_hand)
        
        your_points = totaler(your_hand)
        show_table(your_hand, dealer_hand)
        if your_points < 21:
            hit = int(input('Stand (0) or Hit? (1)'))

            while hit == 1 and your_points < 21:
                print('You chose hit.')
                deal_card_to_player(your_hand, deck)
                your_points = totaler(your_hand)
                show_table(your_hand, dealer_hand)
                if your_points > 21:
                    break
                hit = int(input('Stand (0) or Hit again? (1)'))

            if hit == 0:
                print('You chose stand.')

        # Dealer hidden card is flipped up
        for card in dealer_hand:
            if 'is_hidden' in card:
                del card['is_hidden']
        dealer_points = totaler(dealer_hand)
        determine_outcome(deck, your_hand, dealer_hand, dealer_points, your_points)

        game_running = False


# setup()
