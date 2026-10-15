"""
test_greedy.py - Pruebas del enfoque voraz 

Se ejecuta con:  python test_greedy.py

"""
import random
import time

from particion_greedy import partition_greedy


# ---------------------------------------------------------------------------
# Referencia exacta e independiente (bitset): mejor diferencia posible.
# ---------------------------------------------------------------------------
def optimal_diff(nums):
    total = sum(nums)
    bits = 1  # bit s encendido = suma s alcanzable
    for x in nums:
        bits |= bits << x
    mejor = total
    for s in range(total // 2 + 1):
        if (bits >> s) & 1:
            mejor = min(mejor, total - 2 * s)
    return mejor


# ---------------------------------------------------------------------------
# Casos de prueba
# ---------------------------------------------------------------------------
random.seed(2026)
LISTA_ALEATORIA = [random.randint(1, 100) for _ in range(55)]  # caso extra, 50+ elementos

# Los 5 casos comunes del proyecto: IDENTICOS a los de test_dp.py (Persona 1)
CASOS_COMUNES = [
    ("[1,5,11,5]", [1, 5, 11, 5]),
    ("[1,2,5]", [1, 2, 5]),
    ("[1,2,3]", [1, 2, 3]),
    ("[1,5,10,6]", [1, 5, 10, 6]),
    ("[1..50] (n=50)", list(range(1, 51))),
]

# Contraejemplos donde el voraz FALLA (casos extra acordados con Persona 1)
CONTRAEJEMPLOS = [
    ("[3,3,2,2,2]", [3, 3, 2, 2, 2]),
    ("[4,5,6,7,8]", [4, 5, 6, 7, 8]),
    ("aleatoria de 55", LISTA_ALEATORIA),
]


def try_dp():
    """Devuelve la funcion de la Persona 1 (particion_dinamica) si esta disponible."""
    try:
        from particion_dp import particion_dinamica
        return particion_dinamica
    except Exception:
        return None


def verificar_particion(nums, d, a, b):
    """Chequeos de validez: es una particion real y la diferencia es correcta."""
    assert sorted(a + b) == sorted(nums), "los subconjuntos no reconstruyen la entrada"
    assert abs(sum(a) - sum(b)) == d, "la diferencia reportada no coincide"


def correr():
    dp = try_dp()
    print(f"{'Caso':<24}{'Voraz':>7}{'Optimo':>8}  Resultado")
    print("-" * 52)

    # Casos comunes: verificar validez y que el voraz nunca supere al optimo
    for nombre, nums in CASOS_COMUNES:
        d, a, b = partition_greedy(nums)
        verificar_particion(nums, d, a, b)
        opt = optimal_diff(nums)
        assert d >= opt, "el voraz no puede ser mejor que el optimo"
        if dp:
            assert dp(nums)[0] == opt, "la referencia no coincide con particion_dp"
        estado = "voraz = optimo" if d == opt else "VORAZ FALLA"
        print(f"{nombre:<24}{d:>7}{opt:>8}  {estado}")

    # Contraejemplos: aqui se demuestra que el voraz NO es optimo
    print("-" * 52)
    for nombre, nums in CONTRAEJEMPLOS:
        d, a, b = partition_greedy(nums)
        verificar_particion(nums, d, a, b)
        opt = optimal_diff(nums)
        assert d > opt, f"se esperaba que el voraz fallara en {nombre}"
        if dp:
            assert dp(nums)[0] == opt
        print(f"{nombre:<24}{d:>7}{opt:>8}  VORAZ FALLA (S1={a}, S2={b})")

    # Valores exactos documentados en el analisis
    assert partition_greedy([3, 3, 2, 2, 2])[0] == 2
    assert optimal_diff([3, 3, 2, 2, 2]) == 0
    assert partition_greedy([4, 5, 6, 7, 8])[0] == 4
    assert optimal_diff([4, 5, 6, 7, 8]) == 0
    # [1,5,11,5]: el voraz clasico SI da 0 (no es contraejemplo)
    assert partition_greedy([1, 5, 11, 5])[0] == 0

    # Casos borde
    assert partition_greedy([])[0] == 0
    assert partition_greedy([7])[0] == 7
    assert partition_greedy([4, 4])[0] == 0

    # No debe mutar la entrada
    original = [1, 5, 11, 5]
    copia = list(original)
    partition_greedy(original)
    assert original == copia

    # Tiempo vs tamano de entrada (para el grafico de la Persona 3)
    print("\nTiempo del voraz (promedio de 200 corridas):")
    for n in (10, 20, 30, 40, 50):
        datos = [random.randint(1, 100) for _ in range(n)]
        t0 = time.perf_counter()
        for _ in range(200):
            partition_greedy(datos)
        ms = (time.perf_counter() - t0) / 200 * 1000
        print(f"  n={n:<3} {ms:.5f} ms")

    print("\nTodas las pruebas del voraz pasaron.")


if __name__ == "__main__":
    correr()
