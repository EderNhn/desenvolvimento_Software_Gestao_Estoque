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

# Rota para atualizar estoque
@app.route('/atualizar_estoque', methods=['GET', 'POST'])
def atualizar_estoque():
    if request.method == 'POST':
        cursor = db.cursor()
        nome = request.form['nome']
        quantidade = request.form['quantidade']
        cursor.execute("UPDATE produtos SET quantidade=%s WHERE nome=%s",
                       (quantidade, nome))
        db.commit()
        cursor.close()
        return redirect(url_for('index'))
    return render_template('atualizar_estoque.html')

# Rota para ajustar preço
@app.route('/ajustar_preco', methods=['GET', 'POST'])
def ajustar_preco():
    if request.method == 'POST':
        cursor = db.cursor()
        nome = request.form['nome']
        preco = request.form['preco']
        cursor.execute("UPDATE produtos SET preco=%s WHERE nome=%s",
                       (preco, nome))
        db.commit()
        cursor.close()
        return redirect(url_for('index'))
    return render_template('ajustar_preco.html')

# Rota para remover produto
@app.route('/remover_produto', methods=['GET', 'POST'])
def remover_produto():
    if request.method == 'POST':
        cursor = db.cursor()
        nome = request.form['nome']
        cursor.execute("DELETE FROM produtos WHERE nome=%s", (nome,))
        db.commit()
        cursor.close()
        return redirect(url_for('index'))
    return render_template('remover_produto.html')

if __name__ == '__main__':
    app.run(debug=True)