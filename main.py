# site com os scripts: https://cdnjs.com/
# bibliotecas a instalar: 
# Flask – pip install flask
# Socketio – pip install python-socketio / pip install flask-socketio
# Simple Websocket – pip install simple-websocket

from flask import Flask, render_template  # estruturas para criar o site
from flask_socketio import SocketIO, send  # estruturas para criar o chat

app = Flask(__name__)  # cria o site
app.config[
    "SECRET"] = "ajuiahfa78fh9f78shfs768fgs7f6"  # chave de seguranca, pode ser qualquer coisa, mas escolha algo dificil
app.config[
    "DEBUG"] = True  # para testarmos o código, no final tiramos
socketio = SocketIO(app, cors_allowed_origins="*")  # cria a conexão entre diferentes máquinas que estão no mesmo site


@socketio.on("message")  # define que a função abaixo vai ser acionada quando o evento de "message" acontecer
def gerenciar_mensagens(mensagem):
    print(f"Mensagem: {mensagem}")
    send(mensagem, broadcast=True)  # envia a mensagem para todo mundo conectado no site


@app.route("/")  # cria a página do site
def HomePage():
    return render_template("home_page.html")  # essa página vai carregar esse arquivo html que está aqui


@app.route("/contatos")  # cria a página do site
def Contatos():
    return render_template("contacts.html")  # essa página vai carregar esse arquivo html que está aqui


@app.route("/usuarios/<username>")  # cria a página do site
def Usuarios(username):
    return render_template("users.html", username=username)  # essa página vai carregar esse arquivo html que está aqui

if __name__ == "__main__":
    socketio.run(app, host="192.168.0.20",
                 allow_unsafe_werkzeug=True)  # define que o app vai rodar no seu servidor local, ou seja, na internet em que o seu computador tá conectado
    socketio.run(app, host="192.168.0.20/contatos",
                 allow_unsafe_werkzeug=True)
    socketio.run(app, host="192.168.0.20/usuarios/<username>",
                 allow_unsafe_werkzeug=True)
