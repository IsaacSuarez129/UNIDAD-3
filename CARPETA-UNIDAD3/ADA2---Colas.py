# Problema 1

import queue
import pandas as pd

def llenar_cola():
    cola = queue.Queue()
    i = 1
    datos = []
    while i <= 3:
        dato = input(f"Ingresa el dato {i}: ")
        if i > 3:
            break
        cola.put(int(dato))
        datos.append(int(dato))
        i += 1
    return cola, datos

def sumar_colas(cola1, cola2):
    suma_cola = queue.Queue()
    resultados = []
    while not cola1.empty() and not cola2.empty():
        suma_elementos = cola1.get() + cola2.get()
        suma_cola.put(suma_elementos)
        resultados.append(suma_elementos)
    return suma_cola, resultados

print("[Llenado de cola 1]")
cola1, datos_cola1 = llenar_cola()

print("\n[Llenado de cola 2]")
cola2, datos_cola2 = llenar_cola()

resultado, suma_resultados = sumar_colas(cola1, cola2)

df = pd.DataFrame({
    'Cola 1': datos_cola1,
    'Cola 2': datos_cola2,
    'Resultado': suma_resultados
})

print("Datos ingresados y resultados:")
print(df)


#Problema 2

class Cola:
    def __init__(self):
        self.items = []

    def agregar(self, item):
        self.items.insert(0, item)

    def quitar(self):
        return self.items.pop() if self.items else None

colas = {}

while True:
    opcion = input("Escribe la letra 'C' para agregar un cliente o 'A' para atender a un cliente: ")

    if opcion == 'C':
        servicio = input("Ingresa el número de servicio del cliente: ")
        numero_del_cliente = input("Ingresa el número del cliente: ")
        if servicio not in colas:
            colas[servicio] = Cola()
        colas[servicio].agregar(numero_del_cliente)
        print(f"El cliente {numero_del_cliente} ha sido agregado a la cola de servicio {servicio} exitosamente")

    elif opcion == 'A':
        servicio = input("Ingrese el número de servicio que desea atender: ")
        cliente_atendido = colas[servicio].quitar() if servicio in colas else None
        if cliente_atendido:
            print(f"Atendiendo al cliente {cliente_atendido} del servicio {servicio}")
        else:
            print("No hay clientes en la cola de ese servicio")

    else:
        print("La opcion no es valida, por favor intentalo de nuevo escribiendo C o A")
