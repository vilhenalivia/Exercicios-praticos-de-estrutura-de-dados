usuarios = {
    "João": 25,
    "Maria": 17,
    "Ana": 19,
    "Carlos": 16,
    "Beatriz": 22,
    "Pedro": 15,
    "Luiza": 18
}

# Criação de dicionario que retorna se o usuario é de maior ou já é adulto
classificacao_usuarios = {
    nome: 'Adulto' if idade >= 18 else 'Menor'
    for nome, idade in usuarios.items()
}

# Imprime o dicionario
print('Classificação de usuarios')
print(classificacao_usuarios,)