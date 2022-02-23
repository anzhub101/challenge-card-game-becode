from utils.game import Board

new_game = Board()
new_game.start_game()
print("Would you like to play again?? If so please enter yes! if not enter no. "
      "Also please dont enter anything else because im not as smart as you and will "
      "not understand what it means and potentially go crazy and destroy your computer. Thank you so muc!! :D")
answer = ""
input(answer)
if answer.lower() == "yes":
      another_game = Board()
      another_game.start_game()

else:
      print("See you next time!")