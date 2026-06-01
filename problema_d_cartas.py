import random

# ============================================================
# Problema D – Cartas
# MM3014 Teoría de Probabilidades – Parcial 4
# Experimento: Extraer 2 cartas SIN reemplazo de una baraja de 52 cartas
# Codificación: 0–3 = Ases | 4–51 = Otras cartas (no Ases)
# ============================================================

# Definimos las variables de control de la simulación
SEED = 2026
R    = 10_000

# Inicializamos la semilla del generador aleatorio.
random.seed(SEED)

# Creamos la baraja de 52 cartas como una lista con números del 0 al 51.
# De esta manera, las primeras cuatro cartas (índices 0, 1, 2 y 3) representan los cuatro Ases.
# Cualquier número mayor o igual a 4 representa una carta que no es As.
baraja = list(range(52))

# Contadores de eventos para registrar los resultados
casos_ambos_ases = 0   # Cuenta cuántas veces ambas cartas extraídas resultaron ser Ases.
casos_primer_as = 0    # Cuenta cuántas veces la primera carta extraída resultó ser un As (Evento A).
casos_segundo_as = 0   # Cuenta cuántas veces la segunda carta extraída resultó ser un As (Evento B).

# Bucle principal: repetimos la extracción de dos cartas R veces (10,000 veces).
for _ in range(R):
    # Extraemos 2 cartas de la baraja SIN reemplazo usando random.sample.
    # Esto asegura que no podamos extraer la misma carta física dos veces.
    muestra = random.sample(baraja, 2)
    
    # Comprobamos si la primera carta extraída (muestra[0]) es un As (valor < 4).
    primera_es_as = muestra[0] < 4
    # Comprobamos si la segunda carta extraída (muestra[1]) es un As (valor < 4).
    segunda_es_as = muestra[1] < 4
    
    # Registramos si ocurrió el Evento A (la primera carta es un As).
    if primera_es_as:
        casos_primer_as += 1
        
    # Registramos si ocurrió el Evento B (la segunda carta es un As).
    if segunda_es_as:
        casos_segundo_as += 1
        
    # Registramos si ocurrieron ambos eventos a la vez (ambas cartas son Ases).
    if primera_es_as and segunda_es_as:
        casos_ambos_ases += 1

# Calculamos las probabilidades estimadas
p_ambas_ases = casos_ambos_ases / R   # Estimación de P(A ∩ B)
p_A = casos_primer_as / R            # Estimación de P(A)
p_B = casos_segundo_as / R           # Estimación de P(B)
p_A_por_B = p_A * p_B                # Calculamos el producto de las probabilidades individuales: P(A) * P(B)

# ── PARTE b: Determinar si los eventos son independientes ──
# En teoría de probabilidad, dos eventos A y B son independientes si y solo si:
# P(A ∩ B) = P(A) * P(B).
# Como estamos trabajando con una simulación aleatoria de tamaño finito (R = 10,000), las
# probabilidades estimadas tendrán fluctuaciones de azar.
# Por lo tanto, no evaluamos una igualdad estricta (==), sino si la diferencia absoluta
# entre P(A ∩ B) y P(A)*P(B) es menor que un margen de error tolerable (TOLERANCIA).
TOLERANCIA = 0.0005
son_independientes = abs(p_ambas_ases - p_A_por_B) < TOLERANCIA

# Imprimimos los resultados formateándolos con 4 decimales.
print(f"P(ambas ases) = {p_ambas_ases:.4f}")
print(f"P(A) * P(B) = {p_A_por_B:.4f}")
print(f"Los eventos son independientes: {son_independientes}")


# --------------------- PREGUNTAS PRUEBA -----------------------
# Cada bloque es independiente: vuelve a fijar la semilla (random.seed(SEED))
# para que su resultado sea reproducible por separado.
# Descomenta o ejecuta el archivo completo para ver todas las respuestas.

# NOTA: Para preguntas de palo y figura usamos el modelo COMPLETO de la baraja:
#   valor = carta % 13   ->  0 = As, 1..9 = 2..10, 10 = J, 11 = Q, 12 = K
#   palo  = carta // 13  ->  0 = corazones, 1 = diamantes, 2 = treboles, 3 = espadas
# (Bajo este modelo los cuatro Ases quedan en las posiciones 0, 13, 26 y 39.)
baraja = list(range(52))

# ── PREGUNTA 1: P(al menos 1 As) ─────────────────────────────
random.seed(SEED)
casos = 0
for _ in range(R):
    muestra = random.sample(baraja, 2)
    if muestra[0] % 13 == 0 or muestra[1] % 13 == 0:   # algun As (valor 0)
        casos += 1
print(f"[P1] P(al menos 1 As) = {casos / R:.4f}")

# ── PREGUNTA 2: P(ambas cartas del mismo palo) ───────────────
random.seed(SEED)
casos = 0
for _ in range(R):
    muestra = random.sample(baraja, 2)
    if muestra[0] // 13 == muestra[1] // 13:   # mismo palo
        casos += 1
print(f"[P2] P(mismo palo) = {casos / R:.4f}")

# ── PREGUNTA 3: P(ambas cartas son rojas) ────────────────────
# Roja = corazones (palo 0) o diamantes (palo 1), es decir palo <= 1.
random.seed(SEED)
casos = 0
for _ in range(R):
    muestra = random.sample(baraja, 2)
    if muestra[0] // 13 <= 1 and muestra[1] // 13 <= 1:
        casos += 1
print(f"[P3] P(ambas rojas) = {casos / R:.4f}")

# ── PREGUNTA 4: E[numero de Ases extraidos] ──────────────────
# X puede ser 0, 1 o 2. Acumulamos cuantos Ases salieron en cada extraccion.
random.seed(SEED)
suma_ases = 0
for _ in range(R):
    muestra = random.sample(baraja, 2)
    nro_ases = (1 if muestra[0] % 13 == 0 else 0) + (1 if muestra[1] % 13 == 0 else 0)
    suma_ases += nro_ases
print(f"[P4] E[# de Ases] = {suma_ases / R:.4f}")

# ── PREGUNTA 5: Independencia de A y B ───────────────────────
# A: la primera carta es figura (J, Q o K)  | B: la segunda carta es figura.
# Comparamos P(A y B) con P(A)*P(B); si son (casi) iguales -> independientes.
random.seed(SEED)
casos_A = 0
casos_B = 0
casos_AB = 0
for _ in range(R):
    muestra = random.sample(baraja, 2)
    A = (muestra[0] % 13) >= 10    # primera es figura
    B = (muestra[1] % 13) >= 10    # segunda es figura
    if A:
        casos_A += 1
    if B:
        casos_B += 1
    if A and B:
        casos_AB += 1
p_A = casos_A / R
p_B = casos_B / R
p_AB = casos_AB / R
TOLERANCIA = 0.0005
son_independientes = abs(p_AB - p_A * p_B) < TOLERANCIA
print(f"[P5] P(A) * P(B) = {p_A * p_B:.4f}")
print(f"[P5] P(A y B)    = {p_AB:.4f}")
print(f"[P5] A y B son independientes: {son_independientes}")
