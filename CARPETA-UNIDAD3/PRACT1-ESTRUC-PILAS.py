#Suarez Canche Isaac Moises 3SB

class Pila:
    def __init__(self, cap_max):
        self.items = []
        self.capacidad_maxima = cap_max

    def lista_vacia(self):
        return not self.items

    def lista_llena(self):
        return len(self.items) == self.capacidad_maxima

    def insertar(self, variable):
        if not self.lista_llena():
            self.items.append(variable)
            print(f"Se ha insertado {variable} en la pila.")
        else:
            print("La pila está llena, no se puede insertar otra variable.")

    def eliminar(self):
        if not self.lista_vacia():
            variable_eliminada = self.items.pop()
            print(f"Se ha eliminado {variable_eliminada} de la pila")
        else:
            print("La pila está vacía, no puede ser eliminada")

    def mostrar_estado(self):
        print("Estado de la pila:", self.items)


class realizar_operaciones:
    def __init__(self, pila):
        self.pila = pila

    def operaciones(self, operaciones):
        for operacion, elemento in operaciones:
            if operacion == "Insertar":
                self.pila.insertar(elemento)
            elif operacion == "Eliminar":
                if not self.pila.lista_vacia():
                    self.pila.eliminar()
                else:
                    print("La pila está vacía, no se puede eliminar un elemento.")
            self.pila.mostrar_estado()


pila = Pila(cap_max=8) 
operaciones = realizar_operaciones(pila)

operaciones_list = [("Insertar", "X"), ("Insertar", "Y"), ("Eliminar", None), ("Eliminar", None),
                    ("Eliminar", None), ("Insertar", "V"), ("Insertar", "W"), ("Eliminar", None),
                    ("Insertar", "R")]

operaciones.operaciones(operaciones_list)


## Despues de realizar su ejecucion el codigo, la lista queda con 2 variables.
## En cuanto a problemas de error, no hubo desbordamiento porque la pila nunca alcanzó su capacidad máxima (en este caso es de 8), sin embargo 
## hubo un subdesbordamiento cuando se intentó eliminar elementos de una pila vacía, esto se nota en el tercer intento para eliminar elementos de la pila pero ya estaba vacía.
