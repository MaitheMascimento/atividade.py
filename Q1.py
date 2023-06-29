funcionarios = {}

for i in range(4):
    nome = input("Informe o nome do funcionário: ")
    funcionarios[i+1] = nome

demitirFuncionario = int(input("Informe o número do funcionário que você deseja demitir (1-4): "))

funcionarioDemitido = funcionarios.pop(nFuncionario)

print("Funcionário demitido: \n", funcionarioDemitido)
print("Funcionários restantes:", funcionarios)
