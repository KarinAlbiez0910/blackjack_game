import random
import emoji
from art import logo


print(logo)



deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 'ace']

def start_game():
  want_to_play = input('Do you want to play a game of BlackJack? Type "y" for yes and "n" for no. ')
  if want_to_play == 'y':
    dealer_cards = random.choices(deck, k=2)
    if 'ace' in dealer_cards:
      for entry in dealer_cards:
        if entry == 'ace':
          dealer_cards[dealer_cards.index('ace')] = 11
    dealer_first_card = dealer_cards[0]
    player_cards = random.choices(deck, k=2)
    if 'ace' in player_cards:
      for entry in player_cards:
        if entry == 'ace':
          player_cards[player_cards.index('ace')] = 11
    if dealer_cards == [11, 11]:
      dealer_cards = [11, 1]
    if player_cards == [11, 11]:
      player_cards = [11, 1]
    player_score = sum(player_cards)
    dealer_score = sum(dealer_cards)

    print(f'Your cards: {player_cards}, current score: {player_score}\nDealer\'s first card: {dealer_first_card}')
    if dealer_score == 21:
      print(emoji.emojize(":fire:"))
      print(f'Your final hand: {player_cards}, final score: {player_score}\nDealer\'s final hand: {dealer_cards}, final score: {dealer_score}. BlackJack! The dealer wins.')
      start_game()
    elif player_score == 21:
      print(emoji.emojize(":four_leaf_clover:"))
      print(f'Your final hand: {player_cards}, final score: {player_score}\nDealer\'s final hand: {dealer_cards}, final score: {dealer_score}. BlackJack! You win.')
      start_game()
    else:
      more_cards = True
      while more_cards:
        another_card = input('Type "y" to get another card, "n" to pass. ')

        if another_card == 'y':
          player_next_card = random.choice(deck)
          player_cards.append(player_next_card)
          if 'ace' in player_cards:
            if player_score > 10:
              player_cards[player_cards.index('ace')] = 1
            if player_score <= 10:
              player_cards[player_cards.index('ace')] = 11
            print(player_cards)
          player_score = sum(player_cards)
  
          if dealer_score <= 16:
            dealer_cards.append(random.choice(deck))
            if 'ace' in dealer_cards:
              if dealer_score > 10:
                dealer_cards[dealer_cards.index('ace')] = 1
              if dealer_score <= 10:
                dealer_cards[dealer_cards.index('ace')] = 11
              print(dealer_cards)
            dealer_score = sum(dealer_cards)
    #  print(dealer_cards)
    #  print(dealer_score)
          print(f'Your cards: {player_cards}, current score: {player_score}\nDealer\'s first card: {dealer_first_card}')
          if player_score == 21 and dealer_score != 21:
            print(emoji.emojize(":four_leaf_clover:"))
            print(f'Your final hand: {player_cards}, final score: {player_score}\nDealer\'s final hand: {dealer_cards}, final score: {dealer_score}. You win.')
            more_cards = False
            start_game()
          elif dealer_score == 21 and player_score != 21:
            print(emoji.emojize(":fire:"))
            print(f'Your final hand: {player_cards}, final score: {player_score}\nDealer\'s final hand: {dealer_cards}, final score: {dealer_score}. The dealer wins.')
            more_cards = False
            start_game()
          elif player_score == 21 and dealer_score == 21:
            print(emoji.emojize(":balance_scale:"))
            print(f'Your final hand: {player_cards}, final score: {player_score}\nDealer\'s final hand: {dealer_cards}, final score: {dealer_score}. It\'s a draw.')
            more_cards = False
            start_game()
          elif player_score > 21 and dealer_score<= 20:
            print(emoji.emojize(":fire:"))
            print(f'Your final hand: {player_cards}, final score: {player_score}\nDealer\'s final hand: {dealer_cards}, final score: {dealer_score}. Bust! You went over and lose.')
            more_cards = False
            start_game()
          elif dealer_score > 21 and player_score<= 20:
            print(emoji.emojize(":four_leaf_clover:"))
            print(f'Your final hand: {player_cards}, final score: {player_score}\nDealer\'s final hand: {dealer_cards}, final score: {dealer_score}. Bust! The dealer went over and you win.')
            more_cards = False
            start_game()
          elif dealer_score > 21 and player_score> 21:
            print(emoji.emojize(":balance_scale:"))
            print(f'Your final hand: {player_cards}, final score: {player_score}\nDealer\'s final hand: {dealer_cards}, final score: {dealer_score}. Bust! You both went over, it\'s a draw.')
            more_cards = False
            start_game()

        if another_card == 'n':
          if player_score == dealer_score and player_score < 21:
            print(emoji.emojize(":balance_scale:"))
            print(f'Your final hand: {player_cards}, final score: {player_score}\nDealer\'s final hand: {dealer_cards}, final score: {dealer_score}. It\'s a draw.')
          elif player_score == dealer_score and player_score > 21:
            print(emoji.emojize(":balance_scale:"))
            print(f'Your final hand: {player_cards}, final score: {player_score}\nDealer\'s final hand: {dealer_cards}, final score: {dealer_score}. Bust! You both went over. It\'s a draw!')      
          elif player_score > 21:
            print(emoji.emojize(":fire:"))
            print(f'Your final hand: {player_cards}, final score: {player_score}\nDealer\'s final hand: {dealer_cards}, final score: {dealer_score}. Bust! You went over and lose.')
          elif (player_score == 21 and dealer_score != 21) | player_score > dealer_score:
            print(emoji.emojize(":four_leaf_clover:"))
            print(f'Your final hand: {player_cards}, final score: {player_score}\nDealer\'s final hand: {dealer_cards}, final score: {dealer_score}. You win.')
          elif dealer_score < 21 and dealer_score > player_score:
            print(emoji.emojize(":fire:"))
            print(f'Your final hand: {player_cards}, final score: {player_score}\nDealer\'s final hand: {dealer_cards}, final score: {dealer_score}. The dealer wins.')
          more_cards = False
          start_game()

start_game()
    
      





