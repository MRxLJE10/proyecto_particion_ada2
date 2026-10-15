"""
particion_greedy.py -  enfoque VORAZ para el problema de particion.

Problema: dado un multiconjunto de enteros positivos, dividirlo en dos
subconjuntos S1 y S2 minimizando |sum(S1) - sum(S2)|.

Criterio voraz (clasico, tipo LPT):
  1. Ordenar los numeros de MAYOR a MENOR.
  2. Recorrerlos en ese orden y asignar cada uno al subconjunto que tenga
     la suma actual MENOR (en empate, al primero).

Complejidad:
  Tiempo : O(n log n)  (dominado por el ordenamiento; el recorrido es O(n))
  Espacio: O(n)        (copia ordenada + los dos subconjuntos)

IMPORTANTE: este algoritmo NO garantiza optimalidad. Ejemplo:
  [3, 3, 2, 2, 2] -> voraz da diferencia 2, el optimo es 0 ({3,3} vs {2,2,2}).
"""


def partition_greedy(nums):
    """
    Retorna (diferencia, subconjunto1, subconjunto2).

    - No modifica la lista original.
    - Los subconjuntos se devuelven como listas de los elementos asignados
      (en el orden en que fueron asignados, o sea, de mayor a menor).
    """
    # Paso 1: ordenar descendente (copia, para no mutar la entrada). O(n log n)
    ordenados = sorted(nums, reverse=True)

    subconjunto1, subconjunto2 = [], []
    suma1, suma2 = 0, 0

    # Paso 2: asignar cada numero al subconjunto con menor suma. O(n)
    for x in ordenados:
        if suma1 <= suma2:
            subconjunto1.append(x)
            suma1 += x
        else:
            subconjunto2.append(x)
            suma2 += x

    return abs(suma1 - suma2), subconjunto1, subconjunto2


if __name__ == "__main__":
    for caso in ([1, 5, 11, 5], [1, 2, 5], [1, 2, 3], [1, 5, 10, 6],
                 [3, 3, 2, 2, 2], [4, 5, 6, 7, 8]):
        d, a, b = partition_greedy(caso)
        print(f"{caso} -> diff={d}  S1={a} (suma {sum(a)})  S2={b} (suma {sum(b)})")
