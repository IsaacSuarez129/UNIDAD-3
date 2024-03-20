#Escriba un programa que evalúe, con la ayuda de una pila, una expresión aritmética dada en notación posfija/prefija 

def precedencia_de_operadores(operador):
    if operador == '+' or operador == '-':
        return 1
    elif operador == '*' or operador == '/':
        return 2
    else:
        return 0

def infijo_a_prefijo(expresion):
    operadores = []
    prefijo = []

    for token in reversed(expresion):
        if token.isdigit():
            prefijo.append(token)
        elif token == ')':
            operadores.append(token)
        elif token == '(':
            while operadores[-1] != ')':
                prefijo.append(operadores.pop())
            operadores.pop()
        else:
            while operadores and precedencia_de_operadores(operadores[-1]) > precedencia_de_operadores(token):
                prefijo.append(operadores.pop())
            operadores.append(token)

    while operadores:
        prefijo.append(operadores.pop())

    return ''.join(reversed(prefijo))

def infijo_a_postfijo(expresion):
    operadores = []
    postfijo = []

    for token in expresion:
        if token.isdigit():
            postfijo.append(token)
        elif token == '(':
            operadores.append(token)
        elif token == ')':
            while operadores[-1] != '(':
                postfijo.append(operadores.pop())
            operadores.pop()
        else:
            while operadores and precedencia_de_operadores(operadores[-1]) >= precedencia_de_operadores(token):
                postfijo.append(operadores.pop())
            operadores.append(token)

    while operadores:
        postfijo.append(operadores.pop())
    return ''.join(postfijo)

def main():
    expresion = input("Introduce la expresión aritmética: ")
    print("Expresión en notación prefija:", infijo_a_prefijo(expresion))
    print("Expresión en notación postfija:", infijo_a_postfijo(expresion))

if __name__ == "__main__":
    main()

#Implemente un programa, utilizando la clase Pila que permita la resolución del juego de las Torres de Hanoi para tres discos 

class torre:
    def __init__(self, discos):
        self.num_discos = discos
        self.origen = list(range(discos, 0, -1))
        self.destino = []
        self.intermedio = []

    def colocar_el_disco(self, origen, lugar_a_mover):
        disco = origen.pop()
        lugar_a_mover.append(disco)
        print(f"Se mueve el disco de {origen} a {lugar_a_mover}")

    def mover_la_torre(self, altura, origen, destino, intermedio):
        if altura >= 1:
            self.mover_la_torre(altura - 1, origen, intermedio, destino)
            self.colocar_el_disco(origen, destino)
            self.mover_la_torre(altura - 1, intermedio, destino, origen)

    def solucion_de_la_torre(self):
        self.mover_la_torre(self.num_discos, self.origen, self.destino, self.intermedio)


discos_elegidos = int(input("Escribe el numero de discos con el que se desea jugar: "))
juego = torre(discos_elegidos)
juego.solucion_de_la_torre()
