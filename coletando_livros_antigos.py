catalogo = {
    "Dom Quixote": {"autor": "Miguel de Cervantes", "ano": 1605},
    "Orgulho e Preconceito": {"autor": "Jane Austen", "ano": 1813},
    "O Grande Gatsby": {"autor": "F. Scott Fitzgerald", "ano": 1925},
    "Cem Anos de Solidão": {"autor": "Gabriel García Márquez", "ano": 1967},
    "1984": {"autor": "George Orwell", "ano": 1949},
    "Harry Potter e a Pedra Filosofal": {"autor": "J.K. Rowling", "ano": 1997},
    "O Senhor dos Anéis": {"autor": "J.R.R. Tolkien", "ano": 1954},
    "A Revolução dos Bichos": {"autor": "George Orwell", "ano": 1945},
    "O Apanhador no Campo de Centeio": {"autor": "J.D. Salinger", "ano": 1951},
    "O Código Da Vinci": {"autor": "Dan Brown", "ano": 2003},
}

#Criação de dicionario onde retorna apenas livros com o ano menor que 1950
livros_antigos ={ 
    titulo : info
    for titulo, info in catalogo.items()
    if info['ano'] < 1950
}

#Imprime o dicionario 
print('Livros Antigos:')
print(*livros_antigos,sep='\n')