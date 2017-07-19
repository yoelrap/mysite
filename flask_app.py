from flask import Flask, render_template, session
app = Flask(__name__)
app.config['SECRET_KEY'] = b'2782kjh2kjsy89211'

@app.route('/')
def index():
    return render_template('main.html', the_heading="Hello",
            items=['a', 'second', '7', 'item4'],
            session=session)

@app.route('/start')
def start():
    return 'Lets start a new game!'

@app.route('/choose/<letter>')
def choose(letter):
    # show the user profile for that user
    session['letter'] = letter
    return 'The letter you chose is %s' % letter
