-- Criação do banco de dados:
CREATE DATABASE dbcamara;

-- Definição do banco que usaremos:
USE dbcamara;

-- Tabelas para o cadastro dos dados da caso ocorrido:
CREATE TABLE NaturezasFato(
    id INT AUTO_INCREMENT,
    natureza VARCHAR(50) NOT NULL UNIQUE,
    PRIMARY KEY(id)
);

CREATE TABLE Bairros(
    id INT AUTO_INCREMENT,
    bairro VARCHAR(50) NOT NULL UNIQUE,
    PRIMARY KEY(id)
);

-- CREATE TABLE Cidades(
--     id INT AUTO_INCREMENT,
--     cidade VARCHAR(50) NOT NULL UNIQUE,
--     PRIMARY KEY(id)
-- );

-- CREATE TABLE Estados(
--     id INT AUTO_INCREMENT,
--     uf VARCHAR(50) NOT NULL UNIQUE,
--     PRIMARY KEY(id)
-- );

CREATE TABLE GrausEscolaridade(
    id INT AUTO_INCREMENT,
    grau VARCHAR(30) NOT NULL UNIQUE,
    PRIMARY KEY(id)
);

-- CREATE TABLE Profissoes(
--     id INT AUTO_INCREMENT,
--     profissao VARCHAR(30) NOT NULL UNIQUE,
--     PRIMARY KEY(id)
-- );

CREATE TABLE Racas(
    id INT AUTO_INCREMENT,
    raca VARCHAR(8) NOT NULL UNIQUE,
    PRIMARY KEY(id)
);

CREATE TABLE VitimasAgressores(
    id INT AUTO_INCREMENT,
    idade INT,
    numfilhos INT,
    idgrauescolar INT NOT NULL,
    profissao VARCHAR(50) NOT NULL,
    idraca INT NOT NULL,
    -- geral.
    idbairro INT NOT NULL,
    idnatufato INT NOT NULL,
    -- agressor.
    idadeagressor INT,
    idgrauescolaragressor INT NOT NULL,
    profissaoagressor VARCHAR(50) NOT NULL,
    idracaagressor INT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(idgrauescolar) REFERENCES GrausEscolaridade(id),
    FOREIGN KEY(idgrauescolaragressor) REFERENCES GrausEscolaridade(id),
    -- FOREIGN KEY(idprofissao) REFERENCES Profissoes(id),
    FOREIGN KEY(idraca) REFERENCES Racas(id),
    FOREIGN KEY(idracaagressor) REFERENCES Racas(id),
    FOREIGN KEY(idbairro) REFERENCES Bairros(id),
    FOREIGN KEY(idnatufato) REFERENCES NaturezasFato(id)
);

-- CREATE TABLE Agressores(
--     id INT AUTO_INCREMENT,
--     idade INT,
--     idgrauescolar INT NOT NULL,
--     profissao VARCHAR(50) NOT NULL,
--     idraca INT NOT NULL,
--     idbairro INT NOT NULL,
--     idnatufato INT NOT NULL,
--     PRIMARY KEY(id),
--     FOREIGN KEY(idgrauescolar) REFERENCES GrausEscolaridade(id),
--     FOREIGN KEY(idprofissao) REFERENCES Profissoes(id),
--     FOREIGN KEY(idraca) REFERENCES Racas(id),
--     FOREIGN KEY(idbairro) REFERENCES Bairros(id),
--     FOREIGN KEY(idnatufato) REFERENCES NaturezasFato(id)
-- );
-- CREATE TABLE Registros(
--     id INT AUTO_INCREMENT,
--     idnatufato INT NOT NULL,
--     idvitima INT NOT NULL,
--     idagressor INT NOT NULL,
--     idbairro INT NOT NULL,
--     idcidade INT NOT NULL,
--     iduf INT NOT NULL,
--     PRIMARY KEY(id),
--     FOREIGN KEY(idbairro) REFERENCES Bairros(id),
--     FOREIGN KEY(idcidade) REFERENCES Cidades(id),
--     FOREIGN KEY(iduf) REFERENCES Estados(id),
--     FOREIGN KEY(idnatufato) REFERENCES NaturezasFato(id)
-- );