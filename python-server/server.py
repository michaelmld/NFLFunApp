from flask import Flask, render_template, request, redirect
import nflgame

app = Flask(__name__)

@app.route('/')
def hello_world():
	title = "2016 week 1"
	games = nflgame.games(2016, week=1)
	return render_template('index.html', games=games, title=title)

# @app.route('/signup', methods = ['POST'])
# def signup():
#     email = request.form['email']
#     print("The email address is '" + email + "'")
#     return redirect('/')

if __name__ == '__main__':
    app.run()