class Cola:
    def __init__(self):
        self.items = []
    
    def encolar(self, elemento):
        self.items.append(elemento)
    
    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        return None
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def tamanio(self):
        return len(self.items)


def sumar_colas(cola_a, cola_b):
    resultado = Cola()
    
    while not cola_a.esta_vacia() and not cola_b.esta_vacia():
        a = cola_a.desencolar()
        b = cola_b.desencolar()
        resultado.encolar(a + b)
    
    return resultado


cola_a = Cola()
cola_a.encolar(3)
cola_a.encolar(4)
cola_a.encolar(2)
cola_a.encolar(8)
cola_a.encolar(12)

cola_b = Cola()
cola_b.encolar(6)
cola_b.encolar(2)
cola_b.encolar(9)
cola_b.encolar(11)
cola_b.encolar(3)

cola_resultado = sumar_colas(cola_a, cola_b)

print("Resultado:")
while not cola_resultado.esta_vacia():
    print(cola_resultado.desencolar())