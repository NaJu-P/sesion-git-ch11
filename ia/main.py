import numpy as np
from sklearn.tree import DecisionTreeClassifier # Modelo Supervisado
from sklearn.cluster import KMeans              # Modelo No Supervisado

# --- 1. PREPARACIÓN DE LOS DATOS ---
# Características: [Peso, Textura]
# Los primeros 3 son Manzanas (ligeras, lisas), los últimos 3 son Naranjas (pesadas, rugosas)
X = np.array([
    [140, 1], [130, 2], [150, 1], # Manzanas
    [200, 8], [220, 9], [210, 8]  # Naranjas
])

# Etiquetas: Sabiduría humana (0 es Manzana, 1 es Naranja)
y = np.array([0, 0, 0, 1, 1, 1])

# Fruta nueva misteriosa para probar (Peso 145g, Textura lisa)
fruta_nueva = np.array([[145, 1]])

print(f"--- DATOS ---")
print(f"Fruta nueva a analizar: {fruta_nueva}\n")


# --- 2. ENFOQUE SUPERVISADO (El Maestro) ---
print("--- MODELO SUPERVISADO (Árbol de Decisión) ---")
# Creamos el modelo
modelo_supervisado = DecisionTreeClassifier()

# ENTRENAMIENTO: Le damos X (datos) Y las etiquetas y (respuestas)
modelo_supervisado.fit(X, y)

# PREDICCIÓN
prediccion = modelo_supervisado.predict(fruta_nueva)

if prediccion[0] == 0:
    print(f"Resultado: El modelo dice que es una MANZANA (Etiqueta 0).")
else:
    print(f"Resultado: El modelo dice que es una NARANJA (Etiqueta 1).")
print("Nota: El modelo sabía los nombres porque se los enseñamos.\n")


# --- 3. ENFOQUE NO SUPERVISADO (El Explorador) ---
print("--- MODELO NO SUPERVISADO (K-Means) ---")
# Le pedimos que encuentre 2 grupos (clusters)
modelo_nosupervisado = KMeans(n_clusters=2, random_state=42)

# ENTRENAMIENTO: Solo le damos X. ¡No le damos 'y'! No sabe qué es una manzana.
modelo_nosupervisado.fit(X)

# PREDICCIÓN
grupo = modelo_nosupervisado.predict(fruta_nueva)

print(f"Resultado: El modelo agrupó esta fruta en el GRUPO {grupo[0]}.")
print("Nota: El modelo NO sabe qué es una manzana, solo sabe que esa fruta se parece al Grupo 0.")