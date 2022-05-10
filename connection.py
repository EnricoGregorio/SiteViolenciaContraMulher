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
def setVitimaEAgressor(idade, qtdFilhos, grauEscolaridade, profissao, raca, bairro, natuFato, idadeAgressor, grauEscolaridadeAgressor, profissaoAgressor, racaAgressor):
    with db.cursor() as cursor:
        values = (idade, qtdFilhos, grauEscolaridade, profissao, raca, bairro, natuFato, idadeAgressor, grauEscolaridadeAgressor, profissaoAgressor, racaAgressor)
        query = "INSERT INTO VitimasAgressores(idade, numfilhos, idgrauescolar, profissao, idraca, idbairro, idnatufato, idadeagressor, idgrauescolaragressor, profissaoagressor, idracaagressor) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        try:
            cursor.execute(query, values)
            db.commit()
            return 1
        except pymysql.IntegrityError as err:
            return 0
        
# Cadastro de Agressores:
# def setAgressor(idade, grauEscolaridade, profissao, raca, bairro, natuFato):
#     with db.cursor() as cursor:
#         values = (idade, grauEscolaridade, profissao, raca, bairro, natuFato)
#         query = "INSERT INTO VitimasAgressores(idade, idgrauescolar, profissao, idraca, idbairro, idnatufato) VALUES(%s, %s, %s, %s, %s, %s);"
#         try:
#             cursor.execute(query, values)
#             db.commit()
#             return 1
#         except pymysql.IntegrityError as err:
#             return 0

# Consulta de Alunos:
def getAlunos(matricula):
    with db.cursor() as cursor:
        if matricula == '':
            query = f"SELECT a.matricula, a.aluno, t.turma, c.curso, CASE WHEN a.idade = 0 THEN 'Não' ELSE 'Sim' END AS idade, g.sexo, r.raca, m.meio FROM Alunos AS a INNER JOIN Turmas AS t ON t.id = a.idturma INNER JOIN Cursos AS c ON c.id = a.idcurso INNER JOIN Generos AS g ON g.id = a.idgenero INNER JOIN Racas AS r ON r.id = a.idraca INNER JOIN Transportes AS m ON m.id = a.idtransporte ORDER BY t.turma, c.curso;"
            cursor.execute(query)
            alunos = cursor.fetchall()
            return alunos
        else:
            query = f"SELECT a.matricula, a.aluno, t.turma, c.curso, CASE WHEN a.idade = 0 THEN 'Não' ELSE 'Sim' END AS idade, g.sexo, r.raca, m.meio FROM Alunos AS a INNER JOIN Turmas AS t ON t.id = a.idturma INNER JOIN Cursos AS c ON c.id = a.idcurso INNER JOIN Generos AS g ON g.id = a.idgenero INNER JOIN Racas AS r ON r.id = a.idraca INNER JOIN Transportes AS m ON m.id = a.idtransporte WHERE a.matricula LIKE '%{matricula}%' ORDER BY t.turma, c.curso;"
            cursor.execute(query)
            alunos = cursor.fetchall()
            return alunos
        
# Consulta de quantidade de Alunos:
def getQTDAlunos():
    with db.cursor() as cursor:
        # Querys
        # Turmas
        query1 = "SELECT COUNT(a.matricula) AS alunos FROM Alunos AS a INNER JOIN Turmas AS t ON t.id = a.idturma WHERE t.id = 1;"
        query2 = "SELECT COUNT(a.matricula) AS alunos FROM Alunos AS a INNER JOIN Turmas AS t ON t.id = a.idturma WHERE t.id = 2;"
        query3 = "SELECT COUNT(a.matricula) AS alunos FROM Alunos AS a INNER JOIN Turmas AS t ON t.id = a.idturma WHERE t.id = 3;"
        # Execução das querys
        # Turmas
        cursor.execute(query1)
        val1 = cursor.fetchone()
        cursor.execute(query2)
        val2 = cursor.fetchone()
        cursor.execute(query3)
        val3 = cursor.fetchone()
        # Junte tudo em uma lista e a retorne.
        countAlunos = [val1[0], val2[0], val3[0]]
        return countAlunos