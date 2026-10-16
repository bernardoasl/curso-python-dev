primeiroNome = input("Digite o nome:\n")
segundoNome = input("Digite o sobrenome:\n")

nomeFormatado = f"{segundoNome} {primeiroNome}"
print(nomeFormatado)

texto = "Estudando Python"
palavras = texto.split()
textoInvertido = " ".join(palavras[::-1])
print(textoInvertido)

texto1 = "arara"
texto2 = "azul"

texto1_format = texto1.lower().replace(" ", "")
texto2_format = texto2.lower().replace(" ", "")

palindromo1 = texto1_format == texto1[::-1]
palindromo2 = texto2_format == texto2[::-1]

print(palindromo1)
print(palindromo2)