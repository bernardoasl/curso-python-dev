filmsList = ["Inception", "The Shawshank Redemption", "The Dark Kgnith", "Pulp Fiction", "Interstellar"]

# 1 - Tamanho da Lista
print(len(filmsList))

# 2 - Recuparar um item da lista pelo indice
print(filmsList.index("Interstellar"))

# 3 - Adicionar item no final da lista
filmsList.append("The Lord of the Rings")
print(filmsList)

# 4 - Ordenar a Lista
filmsList.sort()
print(filmsList)

# 5 - Copiar os itens de uma lista para outra
filmsCopy = filmsList.copy()

# 6 - Remove um item especifico
filmsCopy.remove("Pulp Fiction")
print(filmsCopy)

# 7 - Remove todos os itens da lista
filmsList.clear()
print(filmsList)