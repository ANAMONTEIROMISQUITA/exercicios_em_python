# 6. A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.

n = int(input("Digite o número de termos da série de Fibonacci: "))

termo1 = 1
termo2 = 1

print("\n=== Série de Fibonacci ===")

if n == 1:
    print(termo1)
else:
    print(termo1, termo2, end=" ")

    for i in range(3, n + 1):
        proximo = termo1 + termo2
        print(proximo, end=" ")
        termo1 = termo2
        termo2 = proximo