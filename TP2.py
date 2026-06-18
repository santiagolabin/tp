import networkx as nx

import matplotlib.pyplot as plt


# ==========================================================
# CONSTANTES DEL PROBLEMA
# ==========================================================
# K1 representa el costo por kilómetro recorrido
# utilizando hoverboard.
#
# K2 representa el costo por cada tramo recorrido
# utilizando la red de tranvías.
#
# Fórmula general:
# costo = (K1 * km_hoverboard) + (K2 * cantidad_tramos)

K1 = 10   # costo por km en hoverboard
K2 = 5    # costo por tramo de tranvía

# ==========================================================
# GRAFOS
# ==========================================================
# Incorporamos todos los vértices al grafo.
# Existen dos tipos:
#   - Estaciones principales del tranvía
#   - Ubicaciones secundarias de la ciudad
#
# Cada elemento de las listas se convierte en un nodo.
# A su vez agregamos las aristas al grafo. 
# Donde también existen dos tipos:
#   - Aristas de tranvía (origen, destino, tramos)
#   - Aristas de hoverboard (ubicacion, estacion, km)


# ==========================================================
# GRAFO 1 - LINEAL
# ==========================================================

# Nodos principales
estaciones_g1 = ["A", "B", "C", "D", "E", "F", "G", "H"]

# Nodos secundarios
ubicaciones_g1 = [
    "Hospital",
    "Bomberos",
    "Comisaria",
    "Escuela",
    "Universidad",
    "Gasolineria",
    "Restaurante",
    "Cine"
]

# Aristas del tranvía (origen, destino, tramos)

aristas_tranvia_g1 = [
    ("A", "B", 1),
    ("B", "C", 1),
    ("C", "D", 1),
    ("D", "E", 1),
    ("E", "F", 1),
    ("D", "G", 1),
    ("G", "H", 1)
]

# Aristas hoverboard (ubicacion, estacion, km)

aristas_hoverboard_g1 = [
    ("Hospital", "A", 0.8),
    ("Bomberos", "B", 0.7),
    ("Comisaria", "D", 0.9),
    ("Escuela", "F", 0.6),
    ("Universidad", "H", 0.7),
    ("Gasolineria", "G", 0.5),
    ("Restaurante", "C", 0.8),
    ("Cine", "E", 0.9)
]

# ==========================================================
# GRAFO 2 - ÁRBOL
# ==========================================================

# Nodos principales
estaciones_g2 = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]

# Nodos secundarios
ubicaciones_g2 = [
    "Hospital",
    "Bomberos",
    "Comisaria",
    "Escuela",
    "Universidad",
    "Gasolineria",
    "Restaurante",
    "DepartamentoA",
    "DepartamentoB",
    "Cine",
    "Biblioteca"
]

# Aristas del tranvía (origen, destino, tramos)

aristas_tranvia_g2 = [

    ("A", "B", 1),
    ("B", "C", 1),
    ("C", "D", 1),
    ("D", "E", 1),
    ("E", "F", 1),
    ("F", "G", 1),
    ("G", "H", 1),
    ("C", "I", 1),
    ("I", "J", 1),
    ("J", "K", 1),
    ("E", "H", 1)
]

# Aristas hoverboard (ubicacion, estacion, km)

aristas_hoverboard_g2 = [

    ("Hospital", "A", 0.4),
    ("Bomberos", "B", 0.3),
    ("Comisaria", "D", 0.4),
    ("Escuela", "E", 0.2),
    ("Universidad", "F", 0.3),
    ("Gasolineria", "G", 0.1),
    ("Restaurante", "H", 0.1),
    ("DepartamentoA", "K", 0.4),
    ("DepartamentoB", "J", 0.3),
    ("Cine", "I", 0.3),
    ("Biblioteca", "C", 0.3)
]

# ================================================================
# GRAFO 3 - HEPTÁGONO - Utilizar el pos de abajo en visualización
# ================================================================

# Nodos principales
estaciones_g3 = ["A", "B", "C", "D", "E", "F", "G", "H"]

# Nodos secundarios
ubicaciones_g3 = [
        "Hospital",
        "Bomberos",
        "Comisaria",
        "Escuela",
        "Universidad",
        "Gasolineria",
        "Cine"
]

# Aristas del tranvía (origen, destino, tramos)

aristas_tranvia_g3 = [

    # anillo exterior
    ("B", "C", 1),
    ("C", "D", 1),
    ("D", "E", 1),
    ("E", "F", 1),
    ("F", "G", 1),
    ("G", "H", 1),
    ("H", "B", 1),

    # radios hacia el centro
    ("A", "B", 1),
    ("A", "C", 1),
    ("A", "D", 1),
    ("A", "E", 1),
    ("A", "F", 1),
    ("A", "G", 1),
    ("A", "H", 1)
]

# Aristas hoverboard (ubicacion, estacion, km)

aristas_hoverboard_g3 = [

    ("Hospital", "B", 0.5),
    ("Bomberos", "C", 0.5),
    ("Comisaria", "D", 0.5),
    ("Escuela", "E", 0.5),
    ("Universidad", "F", 0.5),
    ("Gasolineria", "G", 0.5),
    ("Cine", "H", 0.5)
]

# ==========================================================
# GRAFO A CARGAR
# ==========================================================

# Cambiar cada grafo solo reescribiendo la parte final (g1,g2,g3)
estaciones = estaciones_g2
ubicaciones = ubicaciones_g2
aristas_tranvia = aristas_tranvia_g2
aristas_hoverboard = aristas_hoverboard_g2

# ==========================================================
# CONSTRUCCIÓN DEL GRAFO BASE
# ==========================================================

# Creamos un grafo no dirigido.
# Se utiliza Graph() porque los desplazamientos
# pueden realizarse en ambos sentidos.
G = nx.Graph()

# Agregamos los nodos correspondientes a las
# estaciones principales de la red de tranvías.
G.add_nodes_from(estaciones)

# Agregamos los nodos correspondientes a las
# ubicaciones secundarias (hospital, cine, etc.).
G.add_nodes_from(ubicaciones)

# Recorremos todas las conexiones de tranvía.
#
# Cada tupla contiene:
#   (estación_origen, estación_destino, cantidad_tramos)
#
# Además de conectar los nodos, almacenamos:
#   - tipo = "tranvia"
#   - tramos = cantidad de tramos recorridos
#
# Esta información será utilizada posteriormente
# para calcular los costos del recorrido.
for origen, destino, tramos in aristas_tranvia:

    G.add_edge(
        origen,
        destino,
        tipo="tranvia",
        tramos=tramos
    )

# Agregar conexiones de hoverboard
for origen, destino, km in aristas_hoverboard:

    G.add_edge(
        origen,
        destino,
        tipo="hoverboard",
        km=km
    )


# ==========================================================
# CONSTRUCCIÓN DEL GRAFO DE COSTOS
# ==========================================================
#
# El algoritmo de Dijkstra trabaja utilizando
# un único peso por arista denominado "weight".
#
# Como en nuestro problema existen dos tipos
# de transporte con fórmulas diferentes:
#
# Hoverboard:
#     costo = K1 * km
#
# Tranvía:
#     costo = K2 * tramos
#
# Creamos un segundo grafo donde cada arista
# almacena directamente el costo final en
# el atributo "weight".
#
# De esta manera Dijkstra puede encontrar
# automáticamente el recorrido de menor costo.
#
# ==========================================================

G_costos = nx.Graph()

for u, v, datos in G.edges(data=True):

    if datos["tipo"] == "hoverboard":
        costo = K1 * datos["km"]
    else:
        costo = K2 * datos["tramos"]

    G_costos.add_edge(
        u,
        v,
        weight=costo
    )


# ==========================================================
# PUNTO 1 - DIJKSTRA
# ==========================================================
#
# Este algoritmo permite encontrar el camino
# de costo mínimo entre un nodo origen y un
# nodo destino.
#
# NetworkX utiliza el atributo "weight" de
# cada arista para calcular dicho costo.
#
# La función devuelve:
#   - la ruta encontrada
#   - el costo total
#   - un grafo que contiene únicamente las
#     aristas pertenecientes a la solución
#
# Esto facilita posteriormente su visualización.
# ==========================================================

def resolver_ruta(origen, destino):
    """
    Calcula la ruta de menor costo utilizando Dijkstra.
    Devuelve:
        - ruta encontrada
        - costo total
        - grafo de la ruta
    """
    # Obtiene la secuencia de nodos que forman el recorrido de menor costo.
    ruta = nx.shortest_path(
        G_costos,
        source=origen,
        target=destino,
        weight="weight"
    )
    # Calcula el costo acumulado del recorrido utilizando los pesos definidos en G_costos.
    costo = nx.shortest_path_length(
        G_costos,
        source=origen,
        target=destino,
        weight="weight"
    )

    print("\n" + "=" * 50)
    print("RUTA DE MENOR COSTO (DIJKSTRA)")
    print("=" * 50)

    print("Origen:", origen)
    print("Destino:", destino)

    print("\nRuta encontrada:")
    print(" -> ".join(ruta))

    print("\nCosto total:", costo)

    # Construimos un nuevo grafo que contendrá únicamente las aristas pertenecientes a la ruta óptima encontrada por Dijkstra.
    G_ruta = nx.Graph()

    for i in range(len(ruta) - 1):

        G_ruta.add_edge(
            ruta[i],
            ruta[i + 1]
        )

    return ruta, costo, G_ruta

ruta_minima, costo_minimo, G_dijkstra = resolver_ruta(
    "Hospital",
    "Cine"
)


# ==========================================================
# PUNTO 2 - KRUSKAL
# ==========================================================
#
# El objetivo es obtener un Árbol Recubridor Mínimo
#
# Conecta todas las estaciones del sistema
# utilizando el menor costo posible y evitando
# ciclos innecesarios.
#
# Este resultado puede interpretarse como la red
# mínima que debería mantenerse operativa para
# garantizar la conexión entre todas las estaciones.
#
# Se utiliza el algoritmo de Kruskal implementado
# por NetworkX.
#
# ==========================================================

G_estaciones = nx.Graph()

for origen, destino, tramos in aristas_tranvia:

    G_estaciones.add_edge(
        origen,
        destino,
        weight=tramos
    )

G_camioneta = nx.minimum_spanning_tree(
    G_estaciones,
    algorithm="kruskal"
)

print("\n")
print("=" * 50)
print("KRUSKAL - ÁRBOL RECUBRIDOR MÍNIMA")
print("=" * 50)

for u, v, datos in G_camioneta.edges(data=True):

    print(
        f"{u} <-> {v} | costo = {datos['weight']}"
    )


# ==========================================================
# VISUALIZACIÓN DE RESULTADOS
# ==========================================================
#
# Se generan tres gráficos:
#
# 1) Grafo completo del sistema.
# 2) Ruta mínima obtenida mediante Dijkstra.
# 3) Árbol recubridor mínimo obtenido mediante Kruskal.
#
# Esto permite comparar visualmente los resultados
# de ambos algoritmos sobre la misma red.
#
# ==========================================================

# Posiciones de los nodos
pos = nx.spring_layout(G, seed=42)

# Habilitar el siguiente código en caso de utilizar el tercer lote de datos y a su vez comentar la línea 342
# pos = {
#    "A": (0, 0),
#
#    "B": (0, 4),
#    "C": (-3.1, 2.5),
#    "D": (-3.9, -0.9),
#    "E": (-1.7, -3.6),
#    "F": (1.7, -3.6),
#    "G": (3.9, -0.9),
#    "H": (3.1, 2.5),
#
#    "Hospital": (0, 6),
#    "Bomberos": (-4.8, 3.5),
#    "Comisaria": (-6, -1.2),
#    "Escuela": (-2.5, -5.5),
#    "Universidad": (2.5, -5.5),
#    "Gasolineria": (6, -1.2),
#    "Cine": (4.8, 3.5)
#}

# ===============================================================
# CREAR LOS 3 GRÁFICOS (Dividir en 3 partes la imagen de salida)
# ===============================================================

fig, axs = plt.subplots(1, 3, figsize=(24, 10))


# ==========================================================
# GRAFO BASE
# ==========================================================

# Colores del grafo base
colores_base = []

for nodo in G.nodes():

    if nodo in estaciones:
        colores_base.append("red")
    else:
        colores_base.append("lightblue")

nx.draw(
    G,
    pos,
    ax=axs[0],
    with_labels=True,
    node_color=colores_base
)

labels = {}

for u, v, datos in G.edges(data=True):

    if datos["tipo"] == "tranvia":
        labels[(u, v)] = f'{datos["tramos"]} tr'
    else:
        labels[(u, v)] = f'{datos["km"]} km'

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=labels,
    ax=axs[0]
)

axs[0].set_title("Grafo Base")


# ==========================================================
# GRAFO DIJKSTRA
# ==========================================================

nx.draw(
    G_dijkstra,
    pos,
    ax=axs[1],
    with_labels=True,
    node_color="lightgreen",
    width=3
)

axs[1].set_title(
    f"Dijkstra\nCosto = {costo_minimo}"
)


# ==========================================================
# GRAFO KRUSKAL
# ==========================================================

nx.draw(
    G_camioneta,
    pos,
    ax=axs[2],
    with_labels=True,
    node_color="red",
    width=3
)

labels_mst = nx.get_edge_attributes(
    G_camioneta,
    "weight"
)

nx.draw_networkx_edge_labels(
    G_camioneta,
    pos,
    edge_labels=labels_mst,
    ax=axs[2]
)

axs[2].set_title("Kruskal")


# ==========================================================
# MOSTRAR RESULTADOS
# ==========================================================

# Ajusta automáticamente los márgenes para evitar
# superposiciones entre gráficos y etiquetas.
plt.tight_layout()

# Muestra la ventana con las tres visualizaciones.
plt.show()
