from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'       # change if your MySQL user is different
app.config['MYSQL_PASSWORD'] = 'Apple123@'       # put your MySQL password here
app.config['MYSQL_DB'] = 'flaskdb'

mysql = MySQL(app)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        mysql.connection.commit()
        cur.close()

        return "✅ Data Saved Successfully!"

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)

