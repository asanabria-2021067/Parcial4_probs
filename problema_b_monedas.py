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


# --------------------- PREGUNTAS PRUEBA -----------------------
# Cada bloque es independiente: vuelve a fijar la semilla (random.seed(SEED))
# para que su resultado sea reproducible por separado.
# Descomenta o ejecuta el archivo completo para ver todas las respuestas.

# ── PREGUNTA 1: P(al menos 2 caras) ──────────────────────────
random.seed(SEED)
casos = 0
for _ in range(R):
    nro_caras = random.randint(0, 1) + random.randint(0, 1) + random.randint(0, 1)
    if nro_caras >= 2:
        casos += 1
print(f"[P1] P(al menos 2 caras) = {casos / R:.4f}")

# ── PREGUNTA 2: E[(numero de caras) - (numero de sellos)] ────
# Si hay 3 monedas: sellos = 3 - caras. Acumulamos la diferencia y promediamos.
random.seed(SEED)
suma_diff = 0
for _ in range(R):
    nro_caras = random.randint(0, 1) + random.randint(0, 1) + random.randint(0, 1)
    nro_sellos = 3 - nro_caras
    suma_diff += (nro_caras - nro_sellos)
print(f"[P2] E[caras - sellos] = {suma_diff / R:.4f}")

# ── PREGUNTA 3: Var[X] = E[X^2] - (E[X])^2 ───────────────────
# Necesitamos acumular X y X^2 para calcular la varianza del numero de caras.
random.seed(SEED)
suma_x = 0
suma_x2 = 0
for _ in range(R):
    nro_caras = random.randint(0, 1) + random.randint(0, 1) + random.randint(0, 1)
    suma_x += nro_caras
    suma_x2 += nro_caras ** 2
e_x = suma_x / R
e_x2 = suma_x2 / R
print(f"[P3] Var[X] = {e_x2 - e_x ** 2:.4f}")

# ── PREGUNTA 4: P(primera moneda cara | exactamente 2 caras) ─
# Condicional: el universo son los casos con exactamente 2 caras (denominador).
random.seed(SEED)
casos_2_caras = 0       # denominador
casos_1ra_cara = 0      # numerador: primera moneda cara Y total 2 caras
for _ in range(R):
    moneda1 = random.randint(0, 1)
    moneda2 = random.randint(0, 1)
    moneda3 = random.randint(0, 1)
    nro_caras = moneda1 + moneda2 + moneda3
    if nro_caras == 2:
        casos_2_caras += 1
        if moneda1 == 1:        # la primera cayo cara
            casos_1ra_cara += 1
print(f"[P4] P(1ra moneda cara | exactamente 2 caras) = {casos_1ra_cara / casos_2_caras:.4f}")

# ── PREGUNTA 5: Tres monedas (2 justas + 1 con DOS CARAS) ────
# Se elige una al azar, se lanza y sale cara. P(sea la de dos caras).
# Codificacion: moneda 0 y 1 = justas | moneda 2 = doble cara (siempre sale cara).
random.seed(SEED)
casos_salio_cara = 0    # denominador: salio cara
casos_doble_cara = 0    # numerador: salio cara Y era la moneda de dos caras
for _ in range(R):
    moneda = random.randint(0, 2)         # elige 0, 1 o 2 al azar
    if moneda == 2:
        resultado = 1                     # la moneda de dos caras SIEMPRE da cara
    else:
        resultado = random.randint(0, 1)  # las justas: 50% cara, 50% cruz
    if resultado == 1:                    # salio cara
        casos_salio_cara += 1
        if moneda == 2:
            casos_doble_cara += 1
print(f"[P5] P(moneda de 2 caras | salio cara) = {casos_doble_cara / casos_salio_cara:.4f}")
