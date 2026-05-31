import random

# ============================================================
# Problema C – Canicas de colores
# MM3014 Teoría de Probabilidades – Parcial 4
# Codificación de colores: 0 = roja | 1 = azul | 2 = verde
# ============================================================

# Definimos las variables de control de la simulación
SEED = 2026
R    = 10_000

# Inicializamos la semilla del generador aleatorio.
random.seed(SEED)

# ── PARTE 1: Una sola caja ──────────────────────────────────
# La caja contiene: 5 rojas (0), 3 azules (1), y 2 verdes (2) para un total de 10 canicas.
# La representamos como una lista de Python de longitud 10.
caja = [0]*5 + [1]*3 + [2]*2

# Contador de éxitos para estimar P(ambas rojas)
casos_ambas_rojas = 0

# Repetimos la simulación R veces
for _ in range(R):
    # Extraemos 2 canicas SIN reemplazo.
    # random.sample(poblacion, k) selecciona k elementos únicos (sin reemplazo) de la lista.
    muestra = random.sample(caja, 2)
    
    # Comprobamos si la primera es roja (0) Y la segunda también es roja (0).
    if muestra[0] == 0 and muestra[1] == 0:
        casos_ambas_rojas += 1

# Estimamos la probabilidad como la frecuencia relativa de éxitos.
p_ambas_rojas = casos_ambas_rojas / R
print(f"P(ambas rojas) = {p_ambas_rojas:.4f}")


# ── PARTE 2: Dos cajas (Probabilidad Condicional) ──────────
# Caja 1: 5 rojas (0), 3 azules (1), 2 verdes (2)
# Caja 2: 2 rojas (0), 5 azules (1), 3 verdes (2)
caja1 = [0]*5 + [1]*3 + [2]*2
caja2 = [0]*2 + [1]*5 + [2]*3

# Contadores de eventos
casos_roja_y_verde = 0    # Denominador de la probabilidad condicional: total de veces que sale 1 roja y 1 verde.
casos_c1_rv = 0      # Numerador: veces en las que salió 1 roja y 1 verde viniendo de la Caja 1.

# Repetimos la simulación R veces. 
# Nota: Como la semilla se fijó una sola vez al inicio del programa, este bucle continúa
# la secuencia de números aleatorios a partir de donde terminó la Parte 1.
for _ in range(R):
    # Paso 1: Elegimos una caja al azar (50% de probabilidad para cada una).
    # random.randint(0, 1) devuelve 0 (Caja 1) o 1 (Caja 2).
    caja_elegida = random.randint(0, 1)
    
    # Determinamos de cuál de las dos listas (cajas) vamos a extraer las canicas.
    caja_actual = caja1 if caja_elegida == 0 else caja2
    
    # Paso 2: Extraemos dos canicas al azar sin reemplazo de la caja seleccionada.
    muestra = random.sample(caja_actual, 2)
    
    # Paso 3: Comprobamos el evento condicionante (salió exactamente una roja y una verde).
    # Dado que solo extraemos dos canicas, si en la muestra hay un '0' (roja) y también
    # hay un '2' (verde), necesariamente son una roja y una verde.
    es_roja_y_verde = (0 in muestra) and (2 in muestra)
    
    if es_roja_y_verde:
        # Si se cumple la condición, incrementamos el contador del denominador.
        casos_roja_y_verde += 1
        
        # Si la caja elegida inicialmente fue la Caja 1 (valor 0), incrementamos el numerador.
        if caja_elegida == 0:
            casos_c1_rv += 1

# Calculamos la probabilidad condicional empírica usando el teorema de Bayes simulado:
# P(Caja 1 | una roja y una verde) = P(Caja 1 y una roja y una verde) / P(una roja y una verde)
p_caja1_dado_rv = casos_c1_rv / casos_roja_y_verde
print(f"P(Caja 1 | una roja y una verde) = {p_caja1_dado_rv:.4f}")
