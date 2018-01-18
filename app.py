from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/mak2275', methods=['GET'])
def mikeKarasev():
    return render_template('mike.html')

if __name__ == '__main__':
    app.run()
