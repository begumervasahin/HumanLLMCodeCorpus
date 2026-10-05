from flask import Flask
app = Flask(__name__)
current_index = 0
def fibonacci(n: int) -> int:
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
@app.route("/")
def home():
    return (
        "Available Routes:<br/>"
        "/previous<br/>"
        "/current<br/>"
        "/next<br/>"
    )
@app.route("/current")
def current_fib():
    global current_index
    return str(fibonacci(current_index))
@app.route("/next")
def next_fib():
    global current_index
    current_index += 1
    return str(fibonacci(current_index))
@app.route("/previous")
def prev_fib():
    global current_index
    if current_index > 0:
        current_index -= 1
    return str(fibonacci(current_index))
if __name__ == '__main__':
    app.run()