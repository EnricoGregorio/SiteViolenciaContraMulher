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

@app.route('/graficos', methods=['GET'])
def showPageGraficos():
    lista = conn.getQTDAlunos()
    pageGraficos = render_template('pageGraficos.html', casos=lista)
    return pageGraficos

# # Página do HUB de notícias.
# @app.route('/noticias', methods=['GET', 'POST'])
# def showPageHub():
#     tabela = conn.getPost()
#     pageHub = render_template('pageNoticias.html', noticias=tabela)
#     if 'userEmail' and 'userPwd' in session:
#         return pageHub + '<script>window.document.querySelector(".loginButton1").style.display = "none"; window.document.querySelector(".loginButton2").style.display = "none";</script>'
#     else:
#         return pageHub
        
# # Página das notícias.
# @app.route('/noticias/<post>', methods=['GET', 'POST'])
# def showPage(post):
#     try:
#         pagePost = render_template(f'pagePosts/{post}')    
#         if 'userEmail' and 'userPwd' in session:
#             return pagePost + '<script>window.document.querySelector(".loginButton1").style.display = "none"; window.document.querySelector(".loginButton2").style.display = "none";</script>'
#         else:
#             return pagePost
#     except:
#         return showErrorPage(post)