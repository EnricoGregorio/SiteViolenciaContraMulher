import pymysql

# Configuração da conexão ao banco de dados.
setDB = {
    'host':'localhost',     # Conexão.
    'user':'root',     # Usuário do banco.
    'password':'', # Senha do Usuário.
    'database':'dbcamara'  # Database.
}

db = pymysql.connect(**setDB)

# Códigos para query no banco:
# Consultar os IDs de grau de escolaridade e de raça para as vítimas e agressores:  
def getIDs(g, r, b, n, g2, r2):
    with db.cursor() as cursor:
        # Pegar o ID do Grau Escolar pelo Grau(g).
        query = "SELECT id FROM GrausEscolaridade WHERE grau = %s;"
        cursor.execute(query, g)
        grauEscolar = cursor.fetchone()
        idGrauEscolar = grauEscolar[0]
        # --------------------------------------------------------
        query = "SELECT id FROM GrausEscolaridade WHERE grau = %s;"
        cursor.execute(query, g2)
        grauEscolar2 = cursor.fetchone()
        idGrauEscolarAgressor = grauEscolar2[0]
        # Pegar o ID da Raça pelo Raca(r).
        query = "SELECT id FROM Racas WHERE raca = %s;"
        cursor.execute(query, r)
        raca = cursor.fetchone()
        idRaca = raca[0]
        # --------------------------------------------------------
        query = "SELECT id FROM Racas WHERE raca = %s;"
        cursor.execute(query, r2)
        raca2 = cursor.fetchone()
        idRacaAgressor = raca2[0]
        # Pegar o ID da Natureza do Fato pela Natureza(n).
        query = "SELECT id FROM NaturezasFato WHERE natureza = %s;"
        cursor.execute(query, n)
        naturezaFato = cursor.fetchone()
        idNaturezaFato = naturezaFato[0]
        # Pegar o ID do Bairro pelo Bairro(b).
        query = "SELECT id FROM Bairros WHERE bairro = %s;"
        cursor.execute(query, b)
        bairro = cursor.fetchone()
        idBairro = bairro[0]
        # Criar uma lista para retornar os dois valores.
        ids = [idGrauEscolar, idRaca, idBairro, idNaturezaFato, idGrauEscolarAgressor, idRacaAgressor]
        return ids

# Cadastro de Vítimas:
def setVitimaEAgressor(mes, idade, qtdFilhos, grauEscolaridade, profissao, raca, bairro, natuFato, idadeAgressor, grauEscolaridadeAgressor, profissaoAgressor, racaAgressor):
    with db.cursor() as cursor:
        values = (mes, idade, qtdFilhos, grauEscolaridade, profissao, raca, bairro, natuFato, idadeAgressor, grauEscolaridadeAgressor, profissaoAgressor, racaAgressor)
        query = "INSERT INTO VitimasAgressores(mesocorrido, idade, numfilhos, idgrauescolar, profissao, idraca, idbairro, idnatufato, idadeagressor, idgrauescolaragressor, profissaoagressor, idracaagressor) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        try:
            cursor.execute(query, values)
            db.commit()
            return 1
        except pymysql.IntegrityError as err:
            return 0

def getGrauEscolarVitima():
    with db.cursor() as cursor:
        # Querys para nosso gráfico de grau escolar das vítimas.
        query1 = "SELECT COUNT(p.idgrauescolar) FROM VitimasAgressores AS p INNER JOIN GrausEscolaridade As g ON g.id = p.idgrauescolar WHERE g.grau = 'Não informado';"
        query2 = "SELECT COUNT(p.idgrauescolar) FROM VitimasAgressores AS p INNER JOIN GrausEscolaridade As g ON g.id = p.idgrauescolar WHERE g.grau = 'Superior completo';"
        query3 = "SELECT COUNT(p.idgrauescolar) FROM VitimasAgressores AS p INNER JOIN GrausEscolaridade As g ON g.id = p.idgrauescolar WHERE g.grau = 'Superior incompleto';"
        query4 = "SELECT COUNT(p.idgrauescolar) FROM VitimasAgressores AS p INNER JOIN GrausEscolaridade As g ON g.id = p.idgrauescolar WHERE g.grau = 'Ensino Médio completo';"
        query5 = "SELECT COUNT(p.idgrauescolar) FROM VitimasAgressores AS p INNER JOIN GrausEscolaridade As g ON g.id = p.idgrauescolar WHERE g.grau = 'Ensino Médio incompleto';"
        query6 = "SELECT COUNT(p.idgrauescolar) FROM VitimasAgressores AS p INNER JOIN GrausEscolaridade As g ON g.id = p.idgrauescolar WHERE g.grau = 'Ensino Fundamental completo';"
        query7 = "SELECT COUNT(p.idgrauescolar) FROM VitimasAgressores AS p INNER JOIN GrausEscolaridade As g ON g.id = p.idgrauescolar WHERE g.grau = 'Ensino Fundamental incompleto';"
        query8 = "SELECT COUNT(p.idgrauescolar) FROM VitimasAgressores AS p INNER JOIN GrausEscolaridade As g ON g.id = p.idgrauescolar WHERE g.grau = 'Lê e escreve';"
        query9 = "SELECT COUNT(p.idgrauescolar) FROM VitimasAgressores AS p INNER JOIN GrausEscolaridade As g ON g.id = p.idgrauescolar WHERE g.grau = 'Analfabeto';"
        query10 = "SELECT COUNT(p.idnatufato) FROM VitimasAgressores AS p INNER JOIN NaturezasFato As n ON n.id = p.idnatufato WHERE n.natureza = 'Violência psicológica (ameaça)';"
        query11 = "SELECT COUNT(p.idnatufato) FROM VitimasAgressores AS p INNER JOIN NaturezasFato As n ON n.id = p.idnatufato WHERE n.natureza = 'Lesão corporal';"
        query12 = "SELECT COUNT(p.idnatufato) FROM VitimasAgressores AS p INNER JOIN NaturezasFato As n ON n.id = p.idnatufato WHERE n.natureza = 'Perseguição';"
        query13 = "SELECT COUNT(p.idnatufato) FROM VitimasAgressores AS p INNER JOIN NaturezasFato As n ON n.id = p.idnatufato WHERE n.natureza = 'Injúria';"
        query14 = "SELECT COUNT(p.idnatufato) FROM VitimasAgressores AS p INNER JOIN NaturezasFato As n ON n.id = p.idnatufato WHERE n.natureza = 'Feminicídio';"
        query15 = "SELECT COUNT(p.idnatufato) FROM VitimasAgressores AS p INNER JOIN NaturezasFato As n ON n.id = p.idnatufato WHERE n.natureza = 'Outra';"
        # Comando para executar e guardar a qtd. de vítimas por grau escolar.
        cursor.execute(query1)
        val1 = cursor.fetchone()
        cursor.execute(query2)
        val2 = cursor.fetchone()
        cursor.execute(query3)
        val3 = cursor.fetchone()
        cursor.execute(query4)
        val4 = cursor.fetchone()
        cursor.execute(query5)
        val5 = cursor.fetchone()
        cursor.execute(query6)
        val6 = cursor.fetchone()
        cursor.execute(query7)
        val7 = cursor.fetchone()
        cursor.execute(query8)
        val8 = cursor.fetchone()
        cursor.execute(query9)
        val9 = cursor.fetchone()
        cursor.execute(query10)
        val10 = cursor.fetchone()
        cursor.execute(query11)
        val11 = cursor.fetchone()
        cursor.execute(query12)
        val12 = cursor.fetchone()
        cursor.execute(query13)
        val13 = cursor.fetchone()
        cursor.execute(query14)
        val14 = cursor.fetchone()
        cursor.execute(query15)
        val15 = cursor.fetchone()
        countQtdVit = [val1[0], val2[0], val3[0], val4[0], val5[0], val6[0], val7[0], val8[0], val9[0], val10[0], val11[0], val12[0], val13[0], val14[0], val15[0]]
        return countQtdVit
