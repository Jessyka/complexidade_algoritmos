

def bfprt(A, p, r, i):
    if p < 0 or r >= len(A) or p > r:
        raise ValueError("p e r devem definir um intervalo válido em A")
    if i < 1 or i > r - p + 1:
        raise ValueError("i deve estar entre 1 e o tamanho do intervalo")

    while True:
        if p == r:
            return p

        menor, maior = particione_bfprt(A, p, r)
        quantidade_menores = menor - p
        quantidade_iguais = maior - menor + 1

        if i <= quantidade_menores:
            r = menor - 1
        elif i <= quantidade_menores + quantidade_iguais:
            return menor
        else:
            i -= quantidade_menores + quantidade_iguais
            p = maior + 1


def particione_bfprt(A, p, r):
    pivo = median_of_medians(A, p, r)
    menor = p
    atual = p
    maior = r

    while atual <= maior:
        if A[atual] < pivo:
            A[menor], A[atual] = A[atual], A[menor]
            menor += 1
            atual += 1
        elif A[atual] > pivo:
            A[atual], A[maior] = A[maior], A[atual]
            maior -= 1
        else:
            atual += 1

    return menor, maior


def median_of_medians(A, p, r):
    tamanho = r - p + 1
    if tamanho <= 5:
        A[p:r + 1] = sorted(A[p:r + 1])
        return A[p + tamanho // 2]

    quantidade_medianas = 0
    for inicio in range(p, r + 1, 5):
        fim = min(inicio + 4, r)
        A[inicio:fim + 1] = sorted(A[inicio:fim + 1])
        mediana = inicio + (fim - inicio) // 2
        destino = p + quantidade_medianas
        A[destino], A[mediana] = A[mediana], A[destino]
        quantidade_medianas += 1

    return median_of_medians(A, p, p + quantidade_medianas - 1)

def merge_sort(A):
    if len(A) > 1:
        mid = len(A) // 2
        L = A[:mid]
        R = A[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1

def main():
    A = [6, 2, 5, 4, 3, 7]
    p = 0
    r = len(A) - 1
    i = 3
    result = bfprt(A, p, r, i)
    print(f"The {i}-th smallest element is at index: {result}, value: {A[result]}")
    print(f"Array after bfprt: {A}")

    merge_sort(A[p:i])
    print(f"Array after merge_sort: {A}")

if __name__ == "__main__":
    main()
