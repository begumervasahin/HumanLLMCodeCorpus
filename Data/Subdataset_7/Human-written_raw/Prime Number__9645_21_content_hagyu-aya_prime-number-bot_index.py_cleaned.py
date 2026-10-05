import os
from bottle import route, run
@route("/")
def fonk1():
    return ""
run(b1 = "0.0.0.0", port=int(os.environ.get("PORT", 5000)))