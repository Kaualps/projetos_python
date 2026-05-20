aluno_pedro = notas = float(input("Digite as notas do aluno: "))
aluno_joao = notas = float(input("Digite as notas do aluno: "))
aluno_maria = notas = float(input("Digite as notas do aluno: "))
def calcular_media(notas):
    media = sum(notas) / len(notas)
    return media
media_aluno1 = calcular_media(aluno_pedro)
media_aluno2 = calcular_media(aluno_joao)
media_aluno3 = calcular_media(aluno_maria)
print("Média do aluno pedro: ", media_aluno1)
print("Média do aluno joão: ", media_aluno2)
print("Média do aluno maria: ", media_aluno3)
