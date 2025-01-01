from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Guess the Number</h1>
        <p>Enter a number between 1 and 10 in the URL like this: /guess/your_number</p>
    '''

@app.route('/guess/<int:number>')
def guess(number):
    correct_number = 7  # Change this to any number between 1 and 10
    if 1 <= number <= 10:
        if number == correct_number:
            return "<h2>Correct! You guessed the number.</h2>"
        else:
            return "<h2>Incorrect. Try again!</h2>"
    else:
        return "<h2>Please enter a valid number between 1 and 10.</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
