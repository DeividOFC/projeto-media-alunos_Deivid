nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"Média: {media:.2f}")  

if media > 6:
    print("Aprovado")
elif 5.0 < media <= 6.0:
    print("Recuperação")
else:
    print("Reprovado")