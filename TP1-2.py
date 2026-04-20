import time
import random

class Vector:
    def __init__(self, vector:list[int]) -> None:
        self.vector = vector
    
    def seleccion(self) -> list:
        ordenar = self.vector.copy()                                                # copia el vector/lista
        n = len (ordenar)
        for i in range(n):                  
            num_menor = i                                                           # asigna el primer valor como el minimo
            for j in range(i + 1, n):
                if  ordenar[j] < ordenar[num_menor]:                                # compara el menor número ya asignado con los demás en la lista
                    num_menor = j
            ordenar[i], ordenar[num_menor] = ordenar[num_menor], ordenar[i]         # intercambia el número mínimo con el valor que todavia no se modificó en la lista 
        return  ordenar
    
    def insercion(self) -> list:
        ordenar = self.vector.copy()                                                # copia el vector/lista
        for i in range(1, len (ordenar)):                                           
            clave = ordenar[i]                                                      # agarra el siguiente numero sin ordenar 
            j = i - 1                                                               # agarra el ultimo numero ya ordenado
            while j >= 0 and ordenar[j] > clave:                                    # desplaza los elementos mayores que la clave hacia la derecha
                ordenar[j + 1] = ordenar[j]                                         # mueve el numero ordenado a la derecha
                j -= 1                                                              
            ordenar[j + 1] = clave                                                  # guarda el numero en su posición
        return  ordenar

    def burbujeo(self) -> list:
        ordenar = self.vector.copy()                                                # copia el vector/lista
        n = len(ordenar)
        for i in range(n):
            for j in range(0, n - i - 1):
                if ordenar[j] > ordenar[j + 1]:                                     # verifica si el número de la izquierda es mayor que el de la derecha
                    ordenar[j], ordenar[j + 1] = ordenar[j + 1], ordenar[j]         # en caso de que lo sea, intercambia el de la derecha con el de la izquierda
        return  ordenar
    
    @staticmethod
    def generar_vector(n, tipo):
        if tipo == "ordenado":
            return list(range(n))
        elif tipo == "inverso":
            return list(range(n, 0, -1))
        elif tipo == "random":
            return [random.randint(0, n) for _ in range(n)]
        else:
            raise ValueError("Tipo de vector inválido")


if __name__ == "__main__":
    datos = Vector.generar_vector(100, "random")

    v = Vector(datos)

    print("Vector:", datos)
    tIni = time.time()
    print("Selección:", v.seleccion())
    tFin = time.time()
    diff = tFin-tIni
    print(f"Tiempo de ejecución: {diff:.20f}")
    print("-----------------------------------------")
    tIni = time.time()
    print("Inserción:", v.insercion())
    tFin = time.time()
    diff = tFin-tIni
    print(f"Tiempo de ejecución: {diff:.20f}")
    print("-----------------------------------------")
    tIni = time.time()
    print("Burbujeo:", v.burbujeo())
    tFin = time.time()
    diff = tFin-tIni
    print(f"Tiempo de ejecución: {diff:.20f}")
    print("-----------------------------------------")