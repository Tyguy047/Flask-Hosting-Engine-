# Created By: Tyler Caselli
# With Help From: Chat GPT & GitHub Copilot

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)