atletas = [
    ("Maria Silva", 1.75, 65),
    ("João Santos", 1.80, 72),
    ("Ana Pereira", 1.68, 58),
    ("Pedro Oliveira", 1.92, 85),
    ("Carlos Lima", 1.85, 78),
    ("Beatriz Souza", 1.70, 60),
    ("Fernanda Costa", 1.62, 55),
    ("Lucas Almeida", 1.88, 82),
    ("Rafaela Gomes", 1.74, 63),
    ("Gustavo Ferreira", 1.90, 88),
    ("Larissa Rocha", 1.66, 57),
    ("Henrique Nunes", 1.83, 76),
    ("Juliana Martins", 1.72, 90),
    ("Ricardo Carvalho", 1.86, 80),
    ("Sofia Alves", 1.64, 54),
    ("Matheus Ribeiro", 1.89, 84),
    ("Camila Duarte", 1.69, 81),
    ("Gabriel Monteiro", 1.77, 73),
    ("Eduarda Farias", 1.71, 62),
    ("Thiago Mendes", 1.84, 79),
]

#Lista criada com a condicional de se o resultado da divisão for maio que 25, o nome do atleta é adicionado na lista
atletas_sobrepeso = [atleta[0] for atleta in atletas if (atleta[2] / atleta[1] ** 2) > 25]

#Imprime o nome dos atletas com sobrepeso
print(f'Atletas com IMC maior que 25: \n{atletas_sobrepeso}')