nomes = ["Ana", "Paulo", "João"]

# Retorne o primeiro elemento da lista
print(nomes[0])
# Retorne o elemento da posição 1
print(nomes[1])
# Retorne o último elemento da lista
print(nomes[-1])
# Alterando uum valor especifico, substituindo por outro
nomes[1] = "Bernardo"
print(nomes)
# Adicionando um novo elemento na lista
nomes.append("Pedro")
print(nomes)
# Mostrando o tamanho da lista
print(len(nomes))
# Removendo um elemento especifico da lista
nomes.remove("João")
print(nomes)