import os
from bottle import route, run
DEFAULT_PORT = 5000
@route("/")
def hello_world():
    return "Hello, World!"
if __name__ == "__main__":
    port = int(os.environ.get("PORT", DEFAULT_PORT))
    run(host="0.0.0.0", port=port)