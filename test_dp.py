"""
test_dp.py - Casos de prueba para particion_dinamica
Se ejecuta con: python test_dp.py
"""
from particion_dp import particion_dinamica

# (nombre, lista, diferencia mínima esperada)
CASOS = [
    ("Caso 1", [1, 5, 11, 5], 0),     # {11} vs {1,5,5}
    ("Caso 2", [1, 2, 5], 2),         # {5} vs {1,2}
    ("Caso 3", [1, 2, 3], 0),         # {3} vs {1,2}
    ("Caso 4", [1, 5, 10, 6], 0),     # {1,10} vs {5,6}
    ("Caso 5 (n=50)", list(range(1, 51)), 1),   # suma 1275 (impar) -> dif. 1
]

# Casos borde adicionales pa probar
CASOS_BORDE = [
    ("Borde: vacío", [], 0), 
    ("Borde: un elemento", [7], 7), 
    ("Borde: dos iguales", [4, 4], 0), 
    ("Borde: con ceros", [0, 0, 3, 0], 3), 
    ("Borde: todos iguales, cantidad impar", [5, 5, 5], 5), 
    ("Borde: un elemento domina", [100, 1, 2, 3], 94), 
    ("Borde: elementos repetidos", [3, 3, 3, 3, 3, 3], 0),
]


def verificar(nombre, nums, esperado):
    dif, s1, s2 = particion_dinamica(nums)
    # 1) la diferencia es la esperada
    assert dif == esperado, f"{nombre}: dif={dif}, esperado={esperado}"
    # 2) los subconjuntos son una partición real de la entrada
    assert sorted(s1 + s2) == sorted(nums), f"{nombre}: no es una partición válida"
    # 3) la diferencia reportada coincide con las sumas reales
    assert abs(sum(s1) - sum(s2)) == dif, f"{nombre}: dif inconsistente"
    print(f"OK  {nombre}: diferencia={dif}  S1={s1 if len(nums) <= 10 else '...'}  "
          f"suma1={sum(s1)} suma2={sum(s2)}")


if __name__ == "__main__":
    print("--- Casos oficiales ---")
    for caso in CASOS:
        verificar(*caso)
    print("\n--- Casos borde ---")
    for caso in CASOS_BORDE:
        verificar(*caso)
    print("\nTodos los casos pasaron.")