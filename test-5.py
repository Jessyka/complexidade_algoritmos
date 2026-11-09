# def menor_custo_passes(dias, custos):
#     if not dias:
#         return 0

#     ultimo_dia = dias[-1]
#     dias_set = set(dias)

#     dp = [0] * (ultimo_dia + 1)

#     for i in range(1, ultimo_dia + 1):
#         if i not in dias_set:
#             dp[i] = dp[i - 1]
#             continue

#         custo_possiveis = []
#         for custo in custos:
#             preco=custo["valor"]
#             duracao=custo["duracao"]

#             dia_anterior=max(0, i - duracao)
#             custo_possiveis.append(dp[dia_anterior] + preco)

#         dp[i] = min(custo_possiveis)


#     return dp[ultimo_dia]
            

# dias = [1, 4, 6, 7, 8, 20]
# custos = [{"valor": 2, "duracao": 1},
#     {"valor": 7, "duracao": 7},
#     {"valor": 15, "duracao": 30}]



# print("custo minimo: ", menor_custo_passes(dias, custos))

def planejar_passes(u, p, d, n, k):

    DP = [0] * (n + 2)
    escolha = [0] * (n + 1)

    # Preenchimento bottom-up
    for i in range(n, 0, -1):

        if u[i] == 0:
            DP[i] = DP[i + 1]

        else:
            melhor_custo = float('inf')

            for j in range(1, k + 1):

                proximo = min(n + 1, i + d[j])

                custo = p[j] + DP[proximo]

                if custo < melhor_custo:
                    melhor_custo = custo
                    escolha[i] = j

            DP[i] = melhor_custo

    # Reconstrução da solução
    compras = []
    i = 1

    while i <= n:

        if u[i] == 0:
            i += 1

        else:
            j = escolha[i]

            compras.append((i, j))

            i = min(n + 1, i + d[j])

    return DP[1], compras


# print("custo minimo: ", menor_custo_passes(dias, custos))

n=6
k=3
u=[0, 1, 0, 1, 1, 1, 0, 0]  # dias de uso (1 para uso, 0 para não uso)
p=[0, 2, 7, 15]  # preços dos passes (índice 0 não é usado)
d=[0, 1, 7, 30]  # durações dos passes (índice 0 não é usado)

resultado, compras = planejar_passes(u, p, d, n, k)
print("Custo mínimo:", resultado)
print("Compras realizadas (dia, tipo de passe):", compras)


