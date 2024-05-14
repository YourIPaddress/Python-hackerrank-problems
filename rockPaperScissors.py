'''
comp_choice            R P S
                       0 1 2
User_choice      R  0  D L W  
                 P  1  W D L
                 S  2  L W D
'''

from random import choice
choices = {
  "R" : 0,
  "P" : 1,
  "S" : 2
}
user_choice = input("Rock Paper or Scissors(R/P/S): ")
comp_choice = choice(list(choices.keys()))
print(f"Computer's choice: {comp_choice}")
results = [["Draw!", "You Lose :(", "You Win!"], ["You Win!", "Draw!", "You Lose :("], ["You Lose :(", "You Win!", "Draw!"]]
print(results[choices[user_choice]][choices[comp_choice]])
