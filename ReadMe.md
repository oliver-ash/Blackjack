# Blackjack Game Project
## How Blackjack Works
- First create deck and shuffle it
- Deal 2 cards to player (face up) and 2 to dealer (1 up, 1 down)
- Player input: stand or hit
- Player is served (stand or hit)
- Dealer's hidden card flipped up
- If dealer's total 17 or over, must stand
- If dealer's total 16 or below, must hit
- If anyone goes over 21, they bust
- Otherwise highest player wins, else tie
## Terminal Game Logic
- Random cards will be drawn
- Dealer cards will show on every time an input is given
- Space bar for 'Hit me'
- V1 no betting and aces worth 11
- V2 betting
- V3 card counting
- V4 declare ace 11 or 1
## Progress

## Next Steps
- ~~Add to Github~~
- ~~While loop for playing the game~~
- ~~Write game logic~~
- Prettifying results
- Clean up code, make more elegant, put all card dealing in a function, def initial_deal(), clean up elifs, add comments
- Write out in ReadMe what the results of any possible scenario would be: this would be the outline for testing
- Handle edge cases
- Create functions for receiving and validating input
- ASCII art cards
- Allowing the game to go multiple rounds
- STRETCH: have a button or input that counts cards and suggests actions, explains why
- STRETCH: betting

## Further learning
- Understand what's happening with the requests http request: how do things talk to eachother (http)
- Build a simple (http) net server
