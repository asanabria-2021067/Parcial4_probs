import random

# ============================================================
# Problema A – Dados
# MM3014 Teoría de Probabilidades – Parcial 4
# Experimento: Simular el lanzamiento de dos dados justos de 6 caras
# ============================================================

# 1. ¿Por qué SEED = 2026?
# La "seed" (semilla) inicializa el generador de números pseudoaleatorios del sistema.
# Los computadores no generan azar real; siguen una fórmula matemática a partir de un valor inicial.
# Si usamos la misma semilla, el computador siempre generará exactamente la misma secuencia de números.
# Esto garantiza la reproductibilidad: que tu profesor, tu compañero o tú obtengan exactamente las
# mismas respuestas al ejecutar el programa (por ejemplo, P(suma = 7) = 0.1642).
SEED = 2026

# 2. ¿Por qué R = 10_000?
# "R" representa el número de réplicas o repeticiones del experimento de simulación (Método de Monte Carlo).
# Según la Ley de los Grandes Números, a mayor número de repeticiones, la probabilidad experimental
# (frecuencia relativa) se aproximará más a la probabilidad teórica exacta (que para la suma 7 es 1/6 ≈ 0.1667).
# R = 10,000 es un estándar balanceado: es lo suficientemente grande para darnos una alta precisión de hasta
# 3 o 4 decimales, y lo suficientemente pequeño para que la computadora lo resuelva en milisegundos.
R = 10_000

# Inicializamos el generador con la semilla requerida antes de hacer cualquier sorteo aleatorio.
random.seed(SEED)

# Inicializamos contadores para registrar los resultados de las R repeticiones.
dados_suma_7 = 0             # Cuenta cuántas veces la suma de los dados es exactamente 7.
casos_al_menos_un_par = 0    # Cuenta en cuántas repeticiones al menos uno de los dos dados es par (el espacio condicionado).
casos_ambas_condiciones = 0   # Cuenta cuántas veces la suma es 7 Y al menos uno de los dados es par.

# Bucle principal: repetimos el experimento de lanzar los dados R veces (10,000 veces).
for _ in range(R):
    # random.randint(1, 6) genera un número entero aleatorio entre 1 y 6 (inclusive), 
    # representando el resultado de lanzar un dado justo de 6 caras.
    dado1 = random.randint(1, 6) # Lanzamiento del primer dado.
    dado2 = random.randint(1, 6) # Lanzamiento del segundo dado.
    
    # Calculamos la suma de las caras de ambos dados.
    suma = dado1 + dado2
    
    # ── PARTE a: Estimar la probabilidad de que la suma sea igual a 7 ──
    # Si la suma en esta simulación es 7, incrementamos nuestro contador de éxitos.
    if suma == 7:
        dados_suma_7 += 1
        
    # ── PARTE b: Estimar P(suma = 7 | al menos uno de los dados es par) ──
    # Primero verificamos si se cumple la condición dada ("dado que al menos uno de los dados es par").
    # Usamos el operador residuo (%) para saber si es par: si el residuo al dividir entre 2 es 0, es par.
    al_menos_un_par = (dado1 % 2 == 0) or (dado2 % 2 == 0)
    
    if al_menos_un_par:
        # Si se cumple la condición, este caso forma parte de nuestro nuevo "universo" de interés (denominador).
        casos_al_menos_un_par += 1
        
        # De este nuevo universo, revisamos si además se cumple que la suma de ambos es 7 (numerador).
        if suma == 7:
            casos_ambas_condiciones += 1

# Calculamos las probabilidades dividiendo los casos favorables entre los casos posibles.
p_suma_7 = dados_suma_7 / R                          # Estimación para la parte (a).
p_cond = casos_ambas_condiciones / casos_al_menos_un_par # Estimación para la parte (b).

# Imprimimos los resultados formateando el número decimal a 4 decimales (:.4f) según lo solicitado.
print(f"P(suma = 7) = {p_suma_7:.4f}")
print(f"P(suma = 7 | al menos un par) = {p_cond:.4f}")


# --------------------- PREGUNTAS PRUEBA -----------------------
# Cada bloque es independiente: vuelve a fijar la semilla (random.seed(SEED))
# para que su resultado sea reproducible por separado.
# Descomenta o ejecuta el archivo completo para ver todas las respuestas.

# ── PREGUNTA 1: P(suma = 8) ──────────────────────────────────
random.seed(SEED)
casos = 0
for _ in range(R):
    if random.randint(1, 6) + random.randint(1, 6) == 8:
        casos += 1
print(f"[P1] P(suma = 8) = {casos / R:.4f}")

# ── PREGUNTA 2: P(la suma es par) ────────────────────────────
random.seed(SEED)
casos = 0
for _ in range(R):
    suma = random.randint(1, 6) + random.randint(1, 6)
    if suma % 2 == 0:           # par si el residuo entre 2 es 0
        casos += 1
print(f"[P2] P(suma par) = {casos / R:.4f}")

# ── PREGUNTA 3: P(|dado1 - dado2| = 2) ───────────────────────
random.seed(SEED)
casos = 0
for _ in range(R):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    if abs(dado1 - dado2) == 2:   # abs() = valor absoluto (la diferencia sin signo)
        casos += 1
print(f"[P3] P(|dado1 - dado2| = 2) = {casos / R:.4f}")

# ── PREGUNTA 4: E[max(dado1, dado2)] ─────────────────────────
# Valor esperado del MAYOR de los dos dados. Acumulamos el mayor y promediamos.
random.seed(SEED)
suma_max = 0
for _ in range(R):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma_max += max(dado1, dado2)   # max() devuelve el mayor de los dos
print(f"[P4] E[max(dado1, dado2)] = {suma_max / R:.4f}")

# ── PREGUNTA 5: P(suma par | dado1 > dado2) ──────────────────
# Condicional: el "universo" son los casos donde dado1 > dado2 (denominador).
random.seed(SEED)
casos_d1_mayor = 0       # denominador: dado1 > dado2
casos_par_y_mayor = 0    # numerador: suma par Y dado1 > dado2
for _ in range(R):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    if dado1 > dado2:
        casos_d1_mayor += 1
        if (dado1 + dado2) % 2 == 0:
            casos_par_y_mayor += 1
print(f"[P5] P(suma par | dado1 > dado2) = {casos_par_y_mayor / casos_d1_mayor:.4f}")
