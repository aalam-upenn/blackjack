from art import logo
import os
import sys
from random import choices, choice
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    print(logo)
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    #exits the game if user types n
    if play_game.lower() == 'n':
        sys.exit("Goodbye!")
    #the game starts if user types y
    else:
        os.system('cls')
        player_cards = []
        computer_cards = []
        for _ in range(2):
            player_cards.append(int(input("enter player card ")))
            computer_cards.append(int(input("enter Computer card ")))
        if sum(player_cards) > 21:
            if 11 in player_cards:
                # find the index of 11
                i = player_cards.index(11)
                # replace 11 with 1
                player_cards = player_cards[:i]+[1]+player_cards[i+1:]
        #computer_cards = choices(cards, k=2)
        if sum(computer_cards) > 21:
            if 11 in computer_cards:
                # find the index of 11
                i = computer_cards.index(11)
                # replace 11 with 1
                computer_cards = computer_cards[:i]+[1]+computer_cards[i+1:]

        print(f"   Your cards {player_cards}, current score: {sum(player_cards)}")
        print(f"   Computer's first card: {computer_cards[0]}")

        while sum(computer_cards) < 17 and sum(player_cards) != 21:
            computer_cards.append(int(input("enter computer card since <17 and not 21 yet: ")))
            if sum(computer_cards)>21 and (11 in computer_cards):
                    i = computer_cards.index(11)
                    # replace 11 with 1
                    computer_cards = computer_cards[:i]+[1]+computer_cards[i+1:]

        while sum(player_cards)<21 and sum(computer_cards)!=21:
            deal_again = input("Type 'y' to get another card, type 'n' to pass: ")
            if deal_again.lower() == 'y':
                player_cards.append(int(input("enter player card since still <21: ")))
                if sum(player_cards)>21 and (11 in player_cards):
                    # find the index of 11
                    i = player_cards.index(11)
                    # replace 11 with 1
                    player_cards = player_cards[:i]+[1]+player_cards[i+1:]
                if sum(player_cards) < 21:
                    print(f"   Your cards {player_cards}, current score: {sum(player_cards)}")
            else:
                break

        possibilities = {
            "win":"You win! \U0001F973",
            "lose":"You lose! \U0001F97A",
            "draw":"Game drawn! \U0001F636"
            }


        if sum(player_cards) > 21 or sum(computer_cards)>21:
            if sum(player_cards)>21 and sum(computer_cards)>21:
                result = possibilities["draw"]
            elif sum(player_cards) > 21:
                result = possibilities["lose"]
            else:
                result = possibilities["win"]
        elif sum(player_cards) == 21 or sum(computer_cards) == 21:
            if sum(computer_cards) == 21 and sum(player_cards) == 21:
                result = possibilities["draw"]
            elif sum(player_cards) == 21:
                result = possibilities["win"]
            else:
                result = possibilities["lose"]
        else:
            if sum(player_cards) == sum(computer_cards):
                result = possibilities["draw"]
            elif sum(player_cards) > sum(computer_cards):
                result = possibilities["win"]
            else:
                result = possibilities["lose"]


        print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
        print(result)
        blackjack()

blackjack()
#"Do you want to play a game of Blackjack? Type 'Y' or 'n': "
