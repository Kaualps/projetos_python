print ("carregando")
print ("Seja bem vindo, coloque seu nome abaixo: ")
nome = input("Digite seu nome: ")
print(f"Seja bem vindo:",nome)
senha = int(input("digite a senha com 6 numeros: "))
senha_correta = 659967
while senha != senha_correta:
    senha = int(input("digite a sua senha:"))
    if senha != senha_correta:
        print("Senha incorreta. Tente novamente.")	
print("Acesso concedido!")
