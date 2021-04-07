from art import logo, vs, goodbye
import random
from game_data import data
from replit import clear

# Game Logo
print(logo)
play = True
# Get the details in option's dictionary
def show_detail(option):
  name = option['name']
  description = option['description']
  country = option['country']
  return f"{name}, {description}, {country}"

# Compare data with user guess to check if user got right?
def compare(guess, option_A, opotion_B):
  if option_A['follower_count'] > option_B['follower_count']:
    return guess == 'a'
  else:
    return guess == 'b'

# Set a replay function and keep trck of the highest score
def play_again(replay):
  if replay == 'y':
    return True
  else:
    return False

highest_score = 0
while play:
  # Generate 2 options from data, start with option_B, then this will become option_A later.
  option_B = random.choice(data)

  # Main code
  is_correct = True
  score = 0
  
  while is_correct:   
    # Generate 2 options from data, here's the real option_B
    option_A = option_B
    option_B = random.choice(data)
    while option_B == option_A:
      option_B = random.choice(data)

    # Print out 2 option details, A vs B
    print(f"Compare A: {show_detail(option_A)}")
    print(vs)
    print(f"Against B: {show_detail(option_B)}")
    # Let user guess which one has more followers
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    # Clear the screen before print out result
    clear()
    print(f"The highest score: {highest_score}")
    print(logo)

    # Compare data with user guess
    is_correct = compare(guess, option_A, option_B)
    if is_correct:
      ## if correct, score +1 and show score
      # When user got correct, option B becomes option A, go back to the start and go next round
      score +=1
      print(f"You're right! Current score: {score}.\n")
    
    
  ## if wrong, show score, ask play again?
  if score > highest_score:
    highest_score = score
  print(f"Sorry, that's wrong. Final score: {score}.\n")
  replay = input("Play again? Type 'Y' or 'N': ").lower()
  play = play_again(replay)
  clear()
  print(f"The highest score: {highest_score}")
  print(logo)

print(goodbye)

### if No, print Goodby Art
### if Yes, show highest score and loop to the beginning

