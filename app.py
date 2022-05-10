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
        # Características gerais.
        natuFato = request.form['natu-fato'].strip()
        bairro = request.form['bairro'].strip()
        # Características da vítima.
        idadeVitima = request.form['idade-vitima'].strip()
        qtdFilhos = request.form['num-filhos'].strip()
        grauEscolarVitima = request.form['grau-escolar-vitima'].strip()
        profissaoVitima = request.form['profissao-vitima'].strip()
        racaVitima = request.form['raca-vitima'].strip()
        # Características do agressor.
        idadeAgressor = request.form['idade-agressor'].strip()
        grauEscolarAgressor = request.form['grau-escolar-agressor'].strip()
        profissaoAgressor = request.form['profissao-agressor'].strip()
        racaAgressor = request.form['raca-agressor'].strip()
        # Consultar IDs de grau de escolaridade e de raça.
        ids = conn.getIDs(grauEscolarVitima, racaAgressor, bairro, natuFato, grauEscolarAgressor, racaVitima)
        # Set vítima.
        result = conn.setVitimaEAgressor(idadeVitima, qtdFilhos, ids[0], profissaoVitima, ids[1], ids[2], ids[3], idadeAgressor, ids[4], profissaoAgressor, ids[5])
        if result == 1:
            return pageDenuncie + '<script>window.alert("Denúncia realizada com sucesso!");</script>'
        else:
            return pageDenuncie + '<script>window.alert("Houve algum erro ao preencher o formulário de denúncia, Por favor, tente novamente.");</script>'
        
@app.route('/graficos', methods=['GET'])
def showPageGraficos():
    lista = conn.getQTDAlunos()
    pageGraficos = render_template('pageGraficos.html', casos=lista)
    return pageGraficos
