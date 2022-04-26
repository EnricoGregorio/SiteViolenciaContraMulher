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

# Cadastros:
        
# Cadastro de Alunos:
def setAluno(matricula, nome, idTurma, idCurso, idade, idGenero, idRaca, idTransporte):
    with db.cursor() as cursor:
        values = (matricula, nome, idTurma, idCurso, idade, idGenero, idRaca, idTransporte)
        query = "INSERT INTO Alunos(matricula, aluno, idturma, idcurso, idade, idgenero, idraca, idtransporte) VALUES(%s, %s, %s, %s, %s, %s, %s, %s);"
        try:
            cursor.execute(query, values)
            db.commit()
            return 1
        except pymysql.IntegrityError as err:
            return 0

# Consultas:  
def getTurmaCursoSexoRacaeMeio(t, c, s, r, m):
    with db.cursor() as cursor:
        # Pegar o ID da turma pela Turma(t).
        query = "SELECT id FROM Turmas WHERE turma = %s;"
        cursor.execute(query, t)
        turma = cursor.fetchone()
        idTurma = turma[0]
        # Pegar o ID do curso pelo Curso(c).
        query = "SELECT id FROM Cursos WHERE curso = %s;"
        cursor.execute(query, c)
        curso = cursor.fetchone()
        idCurso = curso[0]
        # Pegar o ID do sexo pelo Sexo(s).
        query = "SELECT id FROM Generos WHERE sexo = %s;"
        cursor.execute(query, s)
        sexo = cursor.fetchone()
        idSexo = sexo[0]
        # Pegar o ID da raça pelo Raca(r).
        query = "SELECT id FROM Racas WHERE raca = %s;"
        cursor.execute(query, r)
        raca = cursor.fetchone()
        idRaca = raca[0]
        # Pegar o ID do transporte pelo Meio(m).
        query = "SELECT id FROM Transportes WHERE meio = %s;"
        cursor.execute(query, m)
        meio = cursor.fetchone()
        idMeio = meio[0]
        # Criar uma lista para retornar os dois valores.
        sexoTurmaCursoRacaeMeio = [idSexo, idTurma, idCurso, idRaca, idMeio]
        return sexoTurmaCursoRacaeMeio

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