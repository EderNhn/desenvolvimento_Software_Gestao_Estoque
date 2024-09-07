import os
from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

db_password = os.getenv('DB_PASSWORD')

# Configuração do Banco de Dados MySQL
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=db_password,
    database="inventario"
)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('adicionar_produto.html')

# Rota para adicionar produto
@app.route('/adicionar_produto', methods=['GET', 'POST'])
def adicionar_produto():
    if request.method == 'POST':
        cursor = db.cursor()
        nome = request.form['nome']
        descricao = request.form['descricao']
        preco = request.form['preco']
        quantidade = request.form['quantidade']
        cursor.execute("INSERT INTO produtos (nome, descricao, preco, quantidade) VALUES (%s, %s, %s, %s)",
                       (nome, descricao, preco, quantidade))
        db.commit()
        cursor.close()
        return redirect(url_for('index'))
    return render_template('adicionar_produto.html')


if __name__ == '__main__':
    app.run(debug=True)
