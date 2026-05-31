import random

# ============================================================
# Problema B – Monedas
# MM3014 Teoría de Probabilidades – Parcial 4
# Experimento: Simular el lanzamiento de tres monedas justas (cara o cruz)
# ============================================================

# Inicialización de la semilla (para que los números aleatorios se repitan igual en cada ejecución)
# y del número de réplicas R = 10,000 según las especificaciones del examen.
SEED = 2026
R    = 10_000

# Fijamos la semilla aleatoria del generador de la biblioteca estándar de Python.
random.seed(SEED)

# Contadores de eventos
casos_exactamente_2_caras = 0  # Cuenta los experimentos en los que se obtienen exactamente 2 caras.
suma_total_caras = 0           # Suma el número de caras acumulado en las R simulaciones para estimar el valor esperado E[X].

# Bucle principal: ejecutamos el experimento de lanzar 3 monedas R veces (10,000 veces).
for _ in range(R):
    # Simulamos el lanzamiento de las 3 monedas.
    # Usamos la codificación: 0 = cruz, 1 = cara.
    # random.randint(0, 1) tiene un 50% de probabilidad de dar 0 y un 50% de dar 1 (monedas justas).
    moneda1 = random.randint(0, 1)
    moneda2 = random.randint(0, 1)
    moneda3 = random.randint(0, 1)
    
    # El número total de caras en esta repetición es la suma de los lanzamientos
    # (ya que cada cara vale 1 y cada cruz vale 0).
    nro_caras = moneda1 + moneda2 + moneda3
    
    # Acumulamos el número de caras en esta simulación para el cálculo del promedio (valor esperado).
    suma_total_caras += nro_caras
    
    # ── PARTE a: Estimar la probabilidad de obtener exactamente dos caras ──
    # Si el número total de caras obtenidas en este lanzamiento es exactamente 2, incrementamos el contador.
    if nro_caras == 2:
        casos_exactamente_2_caras += 1

# Calculamos los estadísticos finales dividiendo las cantidades acumuladas entre R.
p_2_caras = casos_exactamente_2_caras / R   # Estimación de la probabilidad de obtener exactamente 2 caras.
e_x = suma_total_caras / R                  # Estimación de E[X] (el valor esperado es la media de caras en la simulación).

# Imprimimos los resultados formateados con 4 decimales.
print(f"P(exactamente 2 caras) = {p_2_caras:.4f}")
print(f"E[X] = {e_x:.4f}")
