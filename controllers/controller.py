from flask import render_template, request, redirect
from app import app
from models.game import *
from models.player import *

@app.route('/<string:choice1>/<string:choice2>')
def new_game(choice1, choice2):
    player1 = Player("player1", choice1)
    player2 = Player("player2", choice2)
    game = Game(player1, player2)
    winner = game.find_winner()
    return render_template('base.html', title='Game', winner=winner)



