from flask import Flask, render_template
import mysql.connector, os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "mysqldb"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASS", "root123"),
        database=os.getenv("DB_NAME", "sampledb")
    )

@app.route("/")
def home():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT name FROM users")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", users=[r[0] for r in rows])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

