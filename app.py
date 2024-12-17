from flask import Flask, request, render_template, redirect, url_for
from flask import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def index():
    with open('links.txt', 'r') as f:
        links = f.readlines()
    links = [link.strip() for link in links]
    return render_template('index.html', links=links)

@app.route('/add', methods=['POST'])
def add():
    link = request.form['link']
    save_link(link)
    return redirect(url_for('index'))

@app.before_first_request
def create_tables():
    db.create_all()

def save_link(link):
    with open('links.txt', 'a') as f:
        f.write(link + '\n')


if __name__ == '__main__':
    app.run(debug=True)

