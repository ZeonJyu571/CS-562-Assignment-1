# Blackjack!
# Author: Junyu Meng

import random

# Define the initial settings
player = 0
dealer = 0
outcome = {_: [0,0,0,0] for _ in range(14,22)} # win/push/loss/player points of the round

# Define the pool
decks = ["a","b","c","d","e","f"]
suits = ["heart","diamond","club","spade"]
ranks = ["A",2,3,4,5,6,7,8,9,10,"K","Q","J"]
pool = [rank for deck in decks for suit in suits for rank in ranks ]

# Define drawing a card
def playerDrawCard():
    global pool, player
    # Reshuffle if the pool is down to 50%
    if len(pool) <= 156:
        pool = [rank for deck in decks for suit in suits for rank in ranks]
    card = pool.pop(random.randint(0,len(pool) - 1))
    # Taking care of the Ace and the faces
    if card == "A":
        if player < 11:
            player += 11
            return "A"
        else:
            player += 1
            return "A"
    elif card == "K":
        player += 10
        return "K"
    elif card == "Q":
        player += 10
        return "Q"
    elif card == "J":
        player += 10
        return "J"
    else:
        player += card
        return card

def dealerDrawCard():
    global pool, dealer
    if len(pool) <= 156:
        pool = [rank for deck in decks for suit in suits for rank in ranks]
    card = pool.pop(random.randint(0,len(pool) - 1))
    if card == "A":
        if dealer < 11:
            dealer += 11
            return "A"
        else:
            dealer += 1
            return "A"
    elif card == "K":
        dealer += 10
        return "K"
    elif card == "Q":
        dealer += 10
        return "Q"
    elif card == "J":
        dealer += 10
        return "J"        
    else:
        dealer += card
        return card

# Define the simulation
def simulate(rounds, verbosity):
    global player, dealer

    for _ in range(rounds):
        playerHand = []
        dealerHand = []
        playerStrat = random.randint(14,21)
        for _ in range(2):
            playerHand.append(playerDrawCard())
            dealerHand.append(dealerDrawCard())
        # Print the initial hands
        if verbosity == 2:
            print(f'Initial hand of the player: {playerHand}')
            print(f'Initial hand of the dealer: {dealerHand}')
        
        # Hit and hold
        while player < playerStrat:
            drawnCard = playerDrawCard()
            playerHand.append(drawnCard)
            if verbosity == 2:
                print('Cards received:', drawnCard, end = ' ')
    
        while dealer < player and dealer < 17:
            drawnCard = dealerDrawCard()
            dealerHand.append(drawnCard)
            if verbosity == 2:
                print('Cards received:', drawnCard, end = ' ')
        
        # Counting how many times the current strategy is used
        outcome[playerStrat][3] += 1

        if verbosity == 1 or verbosity == 2:
            print('Player has:', playerHand)
            print('Dealer has:', dealerHand)

        # Determine the winner
        if player > 21 or (player < dealer and dealer < 22):
            outcome[playerStrat][2] += 1
            if verbosity == 1 or verbosity == 2:
                print('Outcome = Loss')
        elif player == dealer and player < 21:
            outcome[playerStrat][1] += 1
            if verbosity == 1 or verbosity == 2:
                print(f'Outcome = Push - both at {player}')
        else:
            outcome[playerStrat][0] += 1
            if verbosity == 1 or verbosity == 2:
                print('Outcome = Win')
     
        # Reset the values
        player = 0
        dealer = 0
    

    probability = {_:[0,0,0] for _ in range(14,22)}

    for key in outcome:
        if outcome[key][3]:
            probability[key][0] = outcome[key][0] / outcome[key][3]
            probability[key][1] = outcome[key][1] / outcome[key][3]
            probability[key][2] = outcome[key][2] / outcome[key][3]

    print(probability)
    return probability

simulate(10000,0)


    
