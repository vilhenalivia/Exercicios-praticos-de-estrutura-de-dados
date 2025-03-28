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
    ("Juliana Martins", 1.72, 59),
    ("Ricardo Carvalho", 1.86, 80),
    ("Sofia Alves", 1.64, 54),
    ("Matheus Ribeiro", 1.89, 84),
    ("Camila Duarte", 1.69, 61),
    ("Gabriel Monteiro", 1.77, 73),
    ("Eduarda Farias", 1.71, 62),
    ("Thiago Mendes", 1.84, 79),
]

#List Comprehension para retornar o valor no indice 1 da lista atletas em uma lista chamada altura
alturas = [atleta[1] for atleta in atletas]

#Calcula a média dos valores de altura dos atletas
atleta_media = sum(alturas) / len(alturas)

#Imprime o valor da média dos atletas
print(f'A média de altura dos atletas é: {atleta_media:.2f}m')