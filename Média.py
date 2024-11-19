soma_notas = 0
num_alunos = int(input("Digite o número de alunos: "))
for i in range(num_alunos):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    soma_notas += nota  
media = soma_notas / num_alunos if num_alunos > 0 else 0
print(f"A média das notas é: {media:.2f}")