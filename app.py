from flask import Flask
from faker import Faker
from waitress import serve

import secrets
app = Flask(__name__)
adjectives = []
colors = []
nouns = []
punctuation = ['.', '!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '|', ';', ':']
fake = Faker()

@app.route('/')
@app.route('/random')
def random():
    global colors, nouns, adjectives
    adjective = secrets.choice(adjectives)
    color = secrets.choice(colors).replace('_', ' ')
    noun = secrets.choice(nouns).replace('_', ' ')
    new_one = adjective + ' ' + color + ' ' + noun + str(fake.random.randint(10, 99)) + secrets.choice(punctuation)
    new_one = new_one.replace('-', ' ').title().replace(' ', '')
    print(new_one)
    return new_one


if __name__ == '__main__':
    print("Loading adjectives!")
    with open('adjectives.csv', newline='') as f:
        for line in f.readlines():
            l = line.strip()
            adjectives.append(l)
    print("Loading colors!")
    with open('colors.csv', newline='') as f:
        for line in f.readlines():
            l = line.strip().split(',')[0]
            colors.append(l)
    print("Loading Nouns!")
    with open('nouns.csv', newline='') as f:
        for line in f.readlines():
            l = line.strip().split(',')[0]
            nouns.append(l)

    random()
    serve(app, host="0.0.0.0", port=8080)
#    app.run()
