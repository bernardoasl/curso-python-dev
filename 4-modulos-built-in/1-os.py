import os

# 1 - Restorna a pasta atual
print(os.getcwd())

# 2 - Listar arquivos e pastas
print(os.listdir())

# 3 - Versão Sistema Operacional
os.system('ver')

# 4 - Configurações da Máquina
os.system('systeminfo')

# 5 - Limpar a Tela do Terminal
os.system('cls')

# 5 - Desligar o PC
os.system('shutdown /s') # Desliga em aproximadamento 1 minuto
os.system('shutdown /s /t 0') # Desliga imediatamente o "0" é o tempo que você quer
os.system('shutdown /a') # Cancela Desligamento do PC

