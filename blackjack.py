import random

def evaluate_hand(hand):
    # Calculate the value of a hand
    value = 0
    num_aces = 0
    
    for card in hand:
        if card in ['K', 'Q', 'J']:
            value += 10
        elif card == 'A':
            value += 11
            num_aces += 1
        else:
            value += int(card)
    
    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1
    
    return value

def basic_strategy_decision(dealer_card, player_hand):
    # Make decision based on basic strategy guidelines
    dealer_card_value = int(dealer_card) if dealer_card.isdigit() else 10
    
    if dealer_card_value in range(2, 7) and evaluate_hand(player_hand) >= 12:
        return "stand"
    elif dealer_card_value in range(7, 11) and evaluate_hand(player_hand) >= 17:
        return "stand"
    elif dealer_card_value in range(2, 7) and evaluate_hand(player_hand) <= 11:
        return "hit"
    elif dealer_card_value in range(7, 11) and evaluate_hand(player_hand) <= 16:
        return "hit"
    else:
        return "hit"  # Follow general hitting/standing guidelines

def play_blackjack():
    # Start the game of blackjack
    print("Let's play Blackjack!")
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    dealer_card = random.choice(deck)
    player_hand = [random.choice(deck), random.choice(deck)]
    
    print("Dealer's face-up card:", dealer_card)
    print("Your hand:", player_hand)
    
    decision = basic_strategy_decision(dealer_card, player_hand)
    
    print("Your decision:", decision)
    
    # Continue playing or end the game based on your requirements
    
play_blackjack()

