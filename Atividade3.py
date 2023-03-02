idade = int(input("Digite a idade da pessoa: "))
autorizacao = input("A pessoa tem autorização dos pais? (sim/não): ")

if idade >= 18 or autorizacao == "sim":
    print("A pessoa pode participar.")
else:
    print("A pessoa não pode participar.")