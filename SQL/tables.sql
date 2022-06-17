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

CREATE TABLE GrausEscolaridade(
    id INT AUTO_INCREMENT,
    grau VARCHAR(30) NOT NULL UNIQUE,
    PRIMARY KEY(id)
);

CREATE TABLE Racas(
    id INT AUTO_INCREMENT,
    raca VARCHAR(8) NOT NULL UNIQUE,
    PRIMARY KEY(id)
);

CREATE TABLE VitimasAgressores(
    -- Vítima
    id INT AUTO_INCREMENT,
    mesocorrido VARCHAR(2) NOT NULL,
    idade INT,
    numfilhos INT,
    idgrauescolar INT NOT NULL,
    profissao VARCHAR(50) NOT NULL,
    idraca INT NOT NULL,
    -- Geral.
    idbairro INT NOT NULL,
    idnatufato INT NOT NULL,
    -- Agressor.
    idadeagressor INT,
    idgrauescolaragressor INT NOT NULL,
    profissaoagressor VARCHAR(50) NOT NULL,
    idracaagressor INT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(idgrauescolar) REFERENCES GrausEscolaridade(id),
    FOREIGN KEY(idgrauescolaragressor) REFERENCES GrausEscolaridade(id),
    FOREIGN KEY(idraca) REFERENCES Racas(id),
    FOREIGN KEY(idracaagressor) REFERENCES Racas(id),
    FOREIGN KEY(idbairro) REFERENCES Bairros(id),
    FOREIGN KEY(idnatufato) REFERENCES NaturezasFato(id)
);
