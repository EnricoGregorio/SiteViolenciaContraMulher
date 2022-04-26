from flask import Flask, render_template, request
import connection as conn

app = Flask(__name__)

# Função para carregar uma página que não existe no site.
@app.route('/<inexistente>', methods=['GET'])
def showErrorPage(inexistente):
    pageError = render_template('pageError404.html')
    return pageError

@app.route('/', methods=['GET'])
def showIndex():
    pageIndex = render_template('index.html')
    return pageIndex