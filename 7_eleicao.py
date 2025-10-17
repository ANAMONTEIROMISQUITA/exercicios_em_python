# 7. Numa eleição existem três candidatos. Faça um programa que peça o
# número total de eleitores. Peça para cada eleitor votar e ao final mostrar o
# número de votos de cada candidato.
# Programa para simular uma eleição com 3 candidatos

total_eleitores = int(input("Digite o número total de eleitores: "))

votos_cand1 = 0
votos_cand2 = 0
votos_cand3 = 0

print("\n=== Candidatos ===")
print("1 - Candidato 1")
print("2 - Candidato 2")
print("3 - Candidato 3")

for i in range(1, total_eleitores + 1):
    voto = int(input(f"\nEleitor {i}, digite o número do seu candidato (1, 2 ou 3): "))

    if voto == 1:
        votos_cand1 += 1
    elif voto == 2:
        votos_cand2 += 1
    elif voto == 3:
        votos_cand3 += 1
    else:
        print("Voto inválido! Este voto não será contabilizado.")

print("\n=== Resultado da Eleição ===")
print(f"Candidato 1: {votos_cand1} votos")
print(f"Candidato 2: {votos_cand2} votos")
print(f"Candidato 3: {votos_cand3} votos")