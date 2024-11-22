from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

def save_link(link):
    with open('links.txt', 'a') as f:
        f.write(link + '\n')

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

if __name__ == '__main__':
    app.run(debug=True)

