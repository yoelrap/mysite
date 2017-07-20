from flask import Flask, render_template, session
import game

app = Flask(__name__)
app.config['SECRET_KEY']=b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    session['state'] = game.reset_state(game.choose_word())
    return render_template('main.html', state=session['state'], letters=game.LETTERS)

@app.route('/turn/<letter>')
def next_turn(letter):
    if 'state' not in session:
        session['state'] = game.reset_state(game.choose_word())
    session['state'] = game.turn(session['state'], letter)
    return render_template('main.html', state=session['state'], letters=game.LETTERS)
