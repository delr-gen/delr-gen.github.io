from flask import Flask
from sqlconnect import create_pool

app = Flask(__name__)

@app.route("/")
def index():        # main page, executes first
    with create_pool().connect() as db_conn:
        # query database
        result = db_conn.execute("SELECT * from Recipe").fetchall()
    #return str([row for row in result])   # what user sees when page loaded
    return "fuck you"


if __name__ == "__main__":
    app.run(host="34.102.94.199", port=8080, debug=True)
