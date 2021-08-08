from models.player import *

class Game():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def winning_choice(self, choice1, choice2):
        if choice1 == "rock" and choice2 == "paper":
            return choice2
        elif choice1 == "rock" and choice2 == "scissors":
            return choice1
        elif choice1 == "scissors" and choice2 == "rock":
            return choice2
        elif choice1 == "scissors" and choice2 == "paper":
            return choice1
        elif choice1 == "paper" and choice2 == "rock":
            return choice1
        elif choice1 == "paper" and choice2 == "scissors":
            return choice2
        else:
            return None
        
        
    def find_winner(self):
        winning_choice = self.winning_choice(self.player1.choice, self.player2.choice)
        if self.player1.choice == winning_choice:
            return self.player1
        elif self.player2.choice == winning_choice:
            return self.player2
        else:
            return None
        