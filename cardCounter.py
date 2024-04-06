from game import create_playing_deck
from game import initial_deal
from game import totaler

# Stipulation: only taking into account the next draw
# You know how many of each card are in the deck
# You know what cards have been dealt, they can't be dealt again
# What is the statistic we would want to know to flip from hit to stand
# P(set of all cards that put you higher than the other person) * P(set of all cards that don't put me over 21 / n remaining cards) > P(3) * P(4)
# P(all cards that don't put you over 21) > P(that of dealer)
# Ex 2 cards left that would put over 21 both at 10. Y: 2&A D: 5&5
# Goal: stay under 21 & get higher score than dealer
# Corresponding stats: P(next card keeps you under 21) & P(next card gets you higher than dealer's including fact dealer will draw again)

deck = create_playing_deck()
your_hand = []
dealer_hand = []

initial_deal(deck, dealer_hand, your_hand)

# Counts the number of cards left in the deck that would keep the player under 21
def under_counter(deck, hand):
    under_cards = []
    for card in deck:
        if card['value'] + totaler(hand) <= 21:
            under_cards.append(card)
    return under_cards

# Counts the number of cards left in the deck that you could draw that would put you over the dealer's current score while staying under 21
def lead_counter(your_hand, dealer_hand, deck):
    lead_gainers = []
    for card in deck:
        if card['value'] + totaler(your_hand) > totaler(dealer_hand) and card['value'] + totaler(your_hand) <= 21:
            lead_gainers.append(card['value'])
    return lead_gainers

# def if_hit():

# def if_stand():

def card_counter(your_hand, dealer_hand, deck): 
    # enter 2 branches: 1 where I hit, one where I stand
    # calculate difference between favorability of me and dealer in branches 1 and 2. 
    # Suggest branch where my favorability higher than dealer's
    # P(all cards that don't put you over 21) > P(that of dealer)
    # Currently cheating unless dealer_hand does not include the face down card
    
    print('Dealer current score')
    print(totaler(dealer_hand))
    if totaler(dealer_hand) < 21 and totaler(dealer_hand) >= 17:
        print('Number of cards dealer could draw that would keep him under 21')
        print(len(under_counter(deck, dealer_hand)))
    print('Your current score')
    print(totaler(your_hand))
    print('Number of cards that would keep you under 21')
    print(len(under_counter(deck, your_hand)))
    print('Number of cards that would get you the lead and keep you under 21')
    print(len(lead_counter(your_hand, dealer_hand, deck)))

    hint = 'HIT'
    return hint

card_counter(your_hand, dealer_hand, deck)


