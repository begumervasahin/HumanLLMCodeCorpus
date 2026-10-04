import os
from bottle import route, run
@route("/")
def hello_world():
    return ""
def main():
    port = int(os.environ.get("PORT", 5000))
    run(host="0.0.0.0", port=port)
if __name__ == "__main__":
    main()