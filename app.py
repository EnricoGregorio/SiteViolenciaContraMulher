from flask import Flask, render_template, request, session, redirect
import connection as conn

app = Flask(__name__)

app.secret_key = "fdjhiiuhrqe9847t8307ht7hqhg"

# Função para enviar os dados do Gestor das notícias para a sessão.
def setGestorUser(user, pwdUser, pageLink):
    if 'gestorLogin' and 'gestorPwd' in session:
        gestorLogin = session['gestorLogin']
        userPwd = session['gestorPwd']
    else:
        session['gestorLogin'] = user
        session['gestorPwd'] = pwdUser
    return redirect(pageLink)

# Função para carregar uma página que não existe no site.
@app.route('/<inexistente>', methods=['GET'])
def showErrorPage(inexistente):
    pageError = render_template('pageError404.html')
    return pageError

@app.route('/', methods=['GET'])
def showIndex():
    pageIndex = render_template('index.html')
    return pageIndex

@app.route('/denuncie', methods=['GET', 'POST'])
def showPageDenuncie():
    pageDenuncie = render_template('pageDenuncie.html')
    if request.method == 'GET':
        return pageDenuncie
    else:
        idadevitmia = request.form['idadevitima'].strip()
        grauescolarvitima = request.form['grauescolarvit'].strip()
        return pageDenuncie

@app.route('/graficos', methods=['GET'])
def showPageGraficos():
    lista = conn.getQTDAlunos()
    pageGraficos = render_template('pageGraficos.html', casos=lista)
    return pageGraficos
