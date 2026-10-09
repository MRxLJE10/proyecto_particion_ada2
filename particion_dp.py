"""
particion_dp.py - Problema de la Partición resuelto con Programación Dinámica

Problema: dado un multiconjunto de enteros no negativos, dividirlo en dos
subconjuntos S1 y S2 tal que |sum(S1) - sum(S2)| sea mínima.

"""

def particion_dinamica(nums):
    
    #Retorna (diferencia_minima, subconjunto1, subconjunto2)

    total = sum(nums)
    mitad = total // 2                     # solo necesitamos sumas hasta S/2

    dp = [False] * (mitad + 1)
    padre = [-1] * (mitad + 1)
    dp[0] = True                          # caso base: suma 0 con el conjunto vacío

    for i, x in enumerate(nums):
        # Se recorre de MAYOR a MENOR para no usar el mismo elemento dos veces
        for s in range(mitad, x - 1, -1): 
            if not dp[s] and dp[s - x]: 
                dp[s] = True
                padre[s] = i

    # Mejor suma alcanzable más cercana a S/2 (la mayor s <= S/2 con dp[s] True)
    mejor = mitad
    while not dp[mejor]:
        mejor -= 1

    idx_subset1 = set() 
    s = mejor
    while s > 0: 
        i = padre[s]
        idx_subset1.add(i)
        s -= nums[i]

    subset1 = [nums[i] for i in range(len(nums)) if i in idx_subset1]
    subset2 = [nums[i] for i in range(len(nums)) if i not in idx_subset1] 
    return total - 2 * mejor, subset1, subset2 


if __name__ == "__main__":
    for caso in ([1, 5, 11, 5], [1, 2, 5], [1, 2, 3], [1, 5, 10, 6]):
        print(caso, "->", particion_dinamica(caso))