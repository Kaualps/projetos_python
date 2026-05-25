
print("-"*40)

numero1 = int(input("Digite o número: "))
numero2 = int(input("Digite o número: "))

print("-"*40)


print("Escolha a operação: ")
print("1 - soma")
print("2 - subrtração")
print("3 - Multiplicação")
print("4 - divisão")

print("-"*40)

operacao = input("Digite o a operação desejada: ")

if operacao == "1":
    resultado = numero1 + numero2
    print(f"O resultado é: {resultado}")
elif operacao == "2":
    resultado = numero1 - numero2
    print(f"O resultado é: {resultado}")
elif operacao == "3":
    resultado = numero1 * numero2
    print(f"O resultado é: {resultado}")
elif operacao == "4":
    resultado = numero1 / numero2
    print(f"O resultado é: {resultado}")

print("-"*40)

