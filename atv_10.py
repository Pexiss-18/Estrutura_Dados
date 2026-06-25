# ============================================================
# Atividade 10 - TwoSum (HashMap)
# Três métodos: Brute Force, Com Ordenação, Com HashMap
# ============================================================


# ── Método 1: Força Bruta ────────────────────────────────────
# Complexidade: O(n²) tempo | O(1) espaço
def two_sum_brute_force(numeros, alvo):
    n = len(numeros)
    for i in range(n):
        for j in range(i + 1, n):
            if numeros[i] + numeros[j] == alvo:
                return [i, j]
    return []


# ── Método 2: Com Ordenação (dois ponteiros) ─────────────────
# Complexidade: O(n log n) tempo | O(n) espaço
def two_sum_ordenacao(numeros, alvo):
    # Guarda o índice original antes de ordenar
    indexados = sorted(enumerate(numeros), key=lambda x: x[1])

    esquerda = 0
    direita = len(indexados) - 1

    while esquerda < direita:
        soma = indexados[esquerda][1] + indexados[direita][1]
        if soma == alvo:
            idx_e = indexados[esquerda][0]
            idx_d = indexados[direita][0]
            return sorted([idx_e, idx_d])
        elif soma < alvo:
            esquerda += 1
        else:
            direita -= 1

    return []


# ── Método 3: Com HashMap ────────────────────────────────────
# Complexidade: O(n) tempo | O(n) espaço
def two_sum(numeros, alvo):
    # mapeia cada valor ao seu índice em `numeros`
    mapa = {}
    for i, valor_atual in enumerate(numeros):
        complemento = alvo - valor_atual
        if complemento in mapa:
            return [mapa[complemento], i]
        mapa[valor_atual] = i
    return []


# ── Testes ───────────────────────────────────────────────────
if __name__ == "__main__":
    casos = [
        ([2, 7, 11, 15], 9),   # → [0, 1]
        ([3, 2, 4],      6),   # → [1, 2]
        ([3, 3],         6),   # → [0, 1]
    ]

    for numeros, alvo in casos:
        print(f"numeros={numeros}  alvo={alvo}")
        print(f"  Brute Force : {two_sum_brute_force(numeros, alvo)}")
        print(f"  Ordenação   : {two_sum_ordenacao(numeros, alvo)}")
        print(f"  HashMap     : {two_sum(numeros, alvo)}")
        print()
