from flask import Flask, jsonify
import random
app = Flask(__name__)
quotes = [
"First they ignore you, then they ridicule you...",
"It works on my machine.",
"The bug is now a feature."
]

@app.route('/')
def hello():
    return 'Hello Thank you for joinin the class'

@app.route('/home')
def get_quote():
    return jsonify({"quote": random.choice(quotes)})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)