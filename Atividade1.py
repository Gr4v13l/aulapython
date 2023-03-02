n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 > n2 + n3 or n2 > n1 + n3 or n3 > n1 + n2:
    print("Pelo menos um dos números é maior que a soma dos outros dois")
else:
    print("Nenhum dos números é maior que a soma dos outros dois números.")