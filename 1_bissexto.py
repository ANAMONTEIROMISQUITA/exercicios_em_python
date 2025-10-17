# 1. Crie um programa que determine se um ano é bissexto com base nas
# regras do calendário gregoriano. Seu programa deve receber um ano como
# entrada e verificar se ele atende às seguintes condições:
# - Um ano é bissexto se for divisível por 4, exceto se também for divisível por 100.
# - Entretanto, se o ano for divisível por 100 e por 400, ele será bissexto.
# Com base nessas regras, implemente a lógica e exiba se o ano fornecido é
# bissexto ou não.

ano = int(input("Digite um ano: "))

def verificar_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

if verificar_bissexto(ano):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")