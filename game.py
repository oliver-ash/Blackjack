import requests

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
    print(source)
    number = requests.get(source)
    print(number)
    number = int(number.text)
    print(number)
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
    print(suits)
    print(denominations)
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

def deal_card_from_deck(deck):
    # Generate a truly random number
    # Remove card from the deck, deck is mutated (if deck is printed line after, deck is changed)
    card = deck.pop(generate_true_random(1, len(deck)))
    return card

new_deck = create_playing_deck()

new_card = deal_card_from_deck(new_deck)
print(new_card)

if new_card in new_deck:
    print('Card not deleted')
else:
    print('Card deleted')




