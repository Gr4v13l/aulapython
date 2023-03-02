n1 = float(input("Digite qual foi sua primeira nota (Entre 0 a 100): "))
n2 = float(input("Digite qual foi sua segunda nota (Entre 0 a 100): "))

soma_n = n1+n2

if soma_n >= 60 and n1 >= 40 and n2 >= 40:
    print("O aluno passou!")
else:
    print("O aluno não passou.")