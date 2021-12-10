import os

def cls():
  os.system("cls" if os.name == "nt" else "clear")

def print_game_state():
  cls()
  print()

  print("Two player game. Each turn, take at least one item from a single pile. You win if you take the last item.\n")

  print("---------------")
  print(f"1st pile: {piles['1']}")
  print(f"2nd pile: {piles['2']}")
  print(f"3rd pile: {piles['3']}")
  print("---------------\n")

def get_pile():
  while True:
    pile = input("Which pile? ")

    if pile not in ["1", "2", "3"]:
      print("Choose 1, 2, or 3.\n")
    elif piles[pile] == 0:
      print(f"Pile {pile} is empty.\n")
    else:
      return pile

def get_amount(pile_amount):
  while True:
    amount = input("How many? ")

    if amount not in ["1", "2", "3", "4", "5"] or int(amount) > pile_amount:
      print("Amount must be a whole number between 1 and the pile amount.\n")
    else:
      return int(amount)

piles = {"1": 3, "2": 4, "3": 5}
game_over = False
player = 1

while not game_over:
  print_game_state()
  print(f"Player {player}:")
  
  pile = get_pile()
  amount = get_amount(piles[pile])
  piles[pile] -= amount

  if sum(piles.values()) == 0:
    game_over = True
    print_game_state()
    print(f"Player {player} wins!")
  else:
    player = 2 if player == 1 else 1
