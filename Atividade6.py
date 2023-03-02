#informações
idade = int(input("Digite sua idade: "))
cat = input("Digite sua categoria (estudante, aposentado, etc.): ")
dia = input("Digite o dia da semana (segunda, terça, etc.): ")

#variável de desconto
desconto = 0

#direito a desconto
if idade >= 60:
    desconto = 0.3
elif cat == "estudante" and (dia == "segunda" or dia == "terça"):
    desconto = 0.2
elif cat == "aposentado":
    desconto = 0.15
elif cat == "professor" and dia == "quarta":
    desconto = 0.25

#resultado
if desconto > 0:
    print("Você tem direito a um desconto de {:.0%}.".format(desconto))
else:
    print("Você não tem direito a desconto.")