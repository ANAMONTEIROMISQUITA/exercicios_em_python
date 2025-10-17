# 8. Jogo de Craps: Crie um programa que simule um jogo de Craps. O jogo funciona da seguinte maneira:
# O jogador lança dois dados, resultando em um valor entre 2 e 12.
# Na primeira jogada:
# - Se o resultado for 7 ou 11, o jogador vence automaticamente (chamado de 'natural').
# - Se o resultado for 2, 3 ou 12, o jogador perde imediatamente (chamado de 'craps').
# - Se o resultado for 4, 5, 6, 8, 9 ou 10, esse valor se torna o Ponto do jogador.
# Caso um 'Ponto' tenha sido estabelecido, o jogador continua lançando os dados:
# - Se tirar o mesmo valor do Ponto, ele vence.
# - Se tirar um 7 antes de repetir o Ponto, ele perde.
# Implemente a lógica para simular esse jogo e exiba o resultado de cada jogada.

import random
import time

def jogar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    print(f"Você tirou {dado1} + {dado2} = {soma}")
    return soma

print("Bem-vindo ao Jogo de Craps!")
input("Pressione ENTER para lançar os dados...")

primeiro_resultado = jogar_dados()

if primeiro_resultado in (7, 11):
    print("Natural! Você venceu!")
elif primeiro_resultado in (2, 3, 12):
    print("Craps! Você perdeu!")
else:
    ponto = primeiro_resultado
    print(f"Seu ponto é {ponto}. Continue jogando até tirar {ponto} novamente!")
    
    while True:
        time.sleep(1.5)
        input("\nPressione ENTER para lançar novamente...")
        resultado = jogar_dados()
        
        if resultado == ponto:
            print("Você tirou o Ponto novamente! Venceu o jogo!")
            break
        elif resultado == 7:
            print("Você tirou 7 antes do Ponto... Perdeu o jogo!")
            break
        else:
            print("Tente novamente...")