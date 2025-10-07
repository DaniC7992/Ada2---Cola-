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


class SistemaAtencion:
    def __init__(self):
        self.colas = {}
        self.contadores = {}
    
    def agregar_servicio(self, num_servicio):
        if num_servicio not in self.colas:
            self.colas[num_servicio] = Cola()
            self.contadores[num_servicio] = 0
    
    def cliente_llega(self, num_servicio):
        if num_servicio not in self.colas:
            self.agregar_servicio(num_servicio)
        
        self.contadores[num_servicio] += 1
        numero_atencion = self.contadores[num_servicio]
        self.colas[num_servicio].encolar(numero_atencion)
        
        print(f"Cliente agregado al servicio {num_servicio}")
        print(f"Número de atención: {numero_atencion}")
    
    def atender_cliente(self, num_servicio):
        if num_servicio not in self.colas:
            print(f"El servicio {num_servicio} no existe")
            return
        
        if self.colas[num_servicio].esta_vacia():
            print(f"No hay clientes en espera para el servicio {num_servicio}")
            return
        
        numero_llamado = self.colas[num_servicio].desencolar()
        print(f"Llamando al cliente número {numero_llamado} del servicio {num_servicio}")
    
    def mostrar_estado(self):
        print("\n--- Estado de las colas ---")
        for servicio in self.colas:
            print(f"Servicio {servicio}: {self.colas[servicio].tamanio()} clientes en espera")
        print()


def main():
    sistema = SistemaAtencion()
    
    print("Sistema de atención de compañía de seguros")
    print("Comandos:")
    print("  C numero_servicio - Cliente llega")
    print("  A numero_servicio - Atender cliente")
    print("  E - Mostrar estado de colas")
    print("  S - Salir")
    print()
    
    while True:
        entrada = input("Ingrese comando: ").strip().upper()
        
        if not entrada:
            continue
        
        partes = entrada.split()
        comando = partes[0]
        
        if comando == 'S':
            print("Saliendo del sistema...")
            break
        
        elif comando == 'E':
            sistema.mostrar_estado()
        
        elif comando == 'C':
            if len(partes) < 2:
                print("Error: Debe ingresar el número de servicio")
                continue
            try:
                num_servicio = int(partes[1])
                sistema.cliente_llega(num_servicio)
            except ValueError:
                print("Error: El número de servicio debe ser un número entero")
        
        elif comando == 'A':
            if len(partes) < 2:
                print("Error: Debe ingresar el número de servicio")
                continue
            try:
                num_servicio = int(partes[1])
                sistema.atender_cliente(num_servicio)
            except ValueError:
                print("Error: El número de servicio debe ser un número entero")
        
        else:
            print("Comando no reconocido")
        
        print()


if __name__ == "__main__":
    main()