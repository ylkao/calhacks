"""from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('home.html')


   """
from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)
 
if __name__ == '__main__':
    app.run()
    """
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/about/')
def about():
    return render_template('about.html')
@app.route('/exercise/')
def exercise():
    return render_template('exercise.html')
@app.route('/food/')
def food():
    return render_template('food.html')
@app.route('/games/')
def games():
    return render_template('games.html')
@app.route('/vent/')
def vent():
    return render_template('vent.html')
if __name__ == '__main__':
    app.run(debug=True)"""