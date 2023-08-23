from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Hello My name is Afzaa!</h2>'


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))