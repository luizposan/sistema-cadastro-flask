from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def conectar_db():
    return sqlite3.connect("database.db")

def criar_tabela():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

criar_tabela()

@app.route("/")
def index():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conn.close()
    return render_template("index.html", clientes=clientes)

@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]

        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO clientes (nome, email) VALUES (?, ?)",
            (nome, email)
        )
        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    return render_template("cadastrar.html")

if __name__ == "__main__":
    app.run(debug=True)
