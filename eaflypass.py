import time

class Nodo:
    def __init__(self, nombre, cedula, categoria):
        self.nombre = nombre
        self.cedula = cedula
        self.categoria = categoria
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.head = None

    def insertar_al_final(self, nombre, cedula, categoria):
        nuevo_nodo = Nodo(nombre, cedula, categoria)
        if not self.head:
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, nombre, cedula, categoria):
        self.items.append((nombre, cedula, categoria))

    def desencolar(self):
        return self.items.pop(0)

    def esta_vacia(self):
        return len(self.items) == 0

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def esta_vacia(self):
        return len(self.items) == 0

class Parqueadero:
    def __init__(self):
        self.lista_estudiantes = ListaEnlazada()
        self.cola_preferencial = Cola()
        self.cola_comun = Cola()
        self.pila_creditos_juan = Pila()
        self.pila_creditos_maria = Pila()

    def registrar_estudiante(self, nombre, cedula, categoria):
        self.lista_estudiantes.insertar_al_final(nombre, cedula, categoria)

    def modificar_creditos(self, estudiante, cantidad):
        if estudiante == "Juan":
            for _ in range(cantidad):
                self.pila_creditos_juan.apilar(estudiante)
        elif estudiante == "Maria":
            for _ in range(cantidad):
                self.pila_creditos_maria.apilar(estudiante)

    def ingresar_parqueadero(self):
        if not self.cola_preferencial.esta_vacia() or not self.cola_comun.esta_vacia():
            if not self.cola_preferencial.esta_vacia():
                estudiante = self.cola_preferencial.desencolar()
                if estudiante[0] == "Juan" and len(self.pila_creditos_juan.items) == 1:
                    print(f"__Alerta__: Estudiante Juan tiene solo 1 crédito. Por favor, recargue más créditos.")
                elif estudiante[0] == "Juan" and len(self.pila_creditos_juan.items) == 0:
                    print(f"__Alerta__: Estudiante Juan no tiene créditos y no tiene permitido el ingreso.")
                    return None
                elif estudiante[0] == "Maria" and len(self.pila_creditos_maria.items) == 1:
                    print(f"__Alerta__: Estudiante Maria tiene solo 1 crédito. Por favor, recargue más créditos.")
                elif estudiante[0] == "Maria" and len(self.pila_creditos_maria.items) == 0:
                    print(f"__Alerta__: Estudiante Maria no tiene créditos y no tiene permitido el ingreso.")
                    return None
                print(f"Atendiendo al estudiante:  {estudiante[0]}.")
                time.sleep(1)
                print(f"   - Créditos: {len(self.pila_creditos_juan.items) if estudiante[0] == 'Juan' else len(self.pila_creditos_maria.items)}")
                time.sleep(1)
                print(f"   - Ingreso a: fila preferencial (matrícula honor)")
                time.sleep(1)
                return estudiante
            elif not self.cola_comun.esta_vacia():
                estudiante = self.cola_comun.desencolar()
                if estudiante[0] == "Juan" and len(self.pila_creditos_juan.items) == 1:
                    print(f"__Alerta__: Estudiante Juan tiene solo 1 crédito. Por favor, recargue más créditos.")
                elif estudiante[0] == "Juan" and len(self.pila_creditos_juan.items) == 0:
                    print(f"__Alerta__: Estudiante Juan no tiene créditos y no tiene permitido el ingreso.")
                    return None
                elif estudiante[0] == "Maria" and len(self.pila_creditos_maria.items) == 1:
                    print(f"__Alerta__: Estudiante Maria tiene solo 1 crédito. Por favor, recargue más créditos.")
                elif estudiante[0] == "Maria" and len(self.pila_creditos_maria.items) == 0:
                    print(f"__Alerta__: Estudiante Maria no tiene créditos y no tiene permitido el ingreso.")
                    return None
                print(f"Atendiendo al estudiante:  {estudiante[0]}.")
                time.sleep(1)
                print(f"   - Créditos: {len(self.pila_creditos_juan.items) if estudiante[0] == 'Juan' else len(self.pila_creditos_maria.items)}")
                time.sleep(1)
                print(f"   - Ingreso a: fila común")
                time.sleep(1)
                return estudiante
        else:
            print("Esperando estudiantes...")
            return None

    def iniciar_sistema(self):
        print("----------------------")
        print("BIENVENIDO A EAFLYPASS")
        print("----------------------")
        intentos = 0
        while intentos < 3:
            estudiante = self.ingresar_parqueadero()
            if estudiante:
                print("Bienvenido a la u!")
                time.sleep(2)
                print("\nReiniciando el sistema...")
                time.sleep(3)
                print("\n")
                print("\n----------------------")
                print("BIENVENIDO A EAFLYPASS")
                print("----------------------")
            else:
                print("\nReiniciando el sistema...")
                time.sleep(3)
                print("\n")
                print("\n----------------------")
                print("BIENVENIDO A EAFLYPASS")
                print("----------------------")
            intentos += 1

# inicio programa
parqueadero = Parqueadero()

# Registrar estudiantes en las colas
parqueadero.cola_preferencial.encolar("Juan", "123456", "preferencial")
parqueadero.cola_comun.encolar("Maria", "789012", "comun")

# Modificar créditos manualmente
parqueadero.modificar_creditos("Juan", 4)
parqueadero.modificar_creditos("Maria", 1)

parqueadero.iniciar_sistema()
