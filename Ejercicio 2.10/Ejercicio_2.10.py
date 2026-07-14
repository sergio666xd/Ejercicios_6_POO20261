from typing import overload

# Sobrecarga de métodos
class Pedido:
    @overload
    def calcular_pedido(self, primer_plato: str, costo_primer_plato: float, bebida: str, costo_bebida: float) -> str:
        ...

    @overload
    def calcular_pedido(self, primer_plato: str, costo_primer_plato: float, segundo_plato: str, costo_segundo_plato: float, bebida: str, costo_bebida: float) -> str:
        ...

    @overload
    def calcular_pedido(self, primer_plato: str, costo_primer_plato: float, segundo_plato: str, costo_segundo_plato: float, bebida: str, costo_bebida: float, postre: str, costo_postre: float) -> str:
        ...


    def calcular_pedido(self, *args) -> str:
        total_args = len(args)

        if total_args == 4:
            primer_plato, costo_primer_plato, bebida, costo_bebida = args
            total = costo_primer_plato + costo_bebida
            return f"El costo de {primer_plato} y {bebida} es = ${total:.2f}"

        elif total_args == 6:
            primer_plato, costo_primer_plato, segundo_plato, costo_segundo_plato, bebida, costo_bebida = args
            total = costo_primer_plato + costo_segundo_plato + costo_bebida
            return f"El costo de {primer_plato}, {segundo_plato} y {bebida} es = ${total:.2f}"

        elif total_args == 8:
            primer_plato, costo_primer_plato, segundo_plato, costo_segundo_plato, bebida, costo_bebida, postre, costo_postre = args
            total = costo_primer_plato + costo_segundo_plato + costo_bebida + costo_postre
            return f"El costo de {primer_plato} + {segundo_plato} + {bebida} + {postre} es = ${total:.2f}"

        else:
            raise TypeError("Cantidad incorrecta de argumentos para calcular_pedido()")


if __name__ == "__main__":
    pedido = Pedido()

    print("Calculador de pedidos\n")
    print("Seleccione el tipo de pedido que desea calcular:\n")
    print("1. Pedido con un plato principal y una bebida")
    print("2. Pedido con un plato principal, un segundo plato y una bebida")
    print("3. Pedido con un plato principal, un segundo plato, una bebida y un postre")

    opcion = int(input("\nIngrese el número de la opción deseada: "))

    # ================= OPCIÓN 1 =================
    if opcion == 1:
        while True:
            try:
                primer_plato = input("Primer plato: ")
                break
            except ValueError:
                print("Por favor, ingrese un nombre válido para el primer plato.")
        while True:
            try:
                costo_primer_plato = float(input("Costo del primer plato: "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido para el costo del primer plato.")
        while True:
            try:
                bebida = input("Bebida: ")
                break
            except ValueError:
                print("Por favor, ingrese un nombre válido para la bebida.")
        while True:
            try:
                costo_bebida = float(input("Costo de la bebida: "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido para el costo de la bebida.")
        
        print("\n" + pedido.calcular_pedido(primer_plato, costo_primer_plato, bebida, costo_bebida))

    # ================= OPCIÓN 2 =================
    elif opcion == 2:
        while True:
            try:
                primer_plato = input("Primer plato: ")
                break
            except ValueError:
                print("Por favor, ingrese un nombre válido para el primer plato.")
        while True:
            try:
                costo_primer_plato = float(input("Costo del primer plato: "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido para el costo del primer plato.")
        while True:
            try:
                segundo_plato = input("Segundo plato: ")
                break
            except ValueError:
                print("Por favor, ingrese un nombre válido para el segundo plato.")
        while True:
            try:
                costo_segundo_plato = float(input("Costo del segundo plato: "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido para el costo del segundo plato.")
        while True:
            try:
                bebida = input("Bebida: ")
                break
            except ValueError:
                print("Por favor, ingrese un nombre válido para la bebida.")
        while True:
            try:
                costo_bebida = float(input("Costo de la bebida: "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido para el costo de la bebida.")
        
        print("\n" + pedido.calcular_pedido(primer_plato, costo_primer_plato, segundo_plato, costo_segundo_plato, bebida, costo_bebida))

    # ================= OPCIÓN 3 =================
    elif opcion == 3:
        while True:
            try:
                primer_plato = input("Primer plato: ")
                break
            except ValueError:
                print("Por favor, ingrese un nombre válido para el primer plato.")
        while True:
            try:
                costo_primer_plato = float(input("Costo del primer plato: "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido para el costo del primer plato.")
        while True:
            try:
                segundo_plato = input("Segundo plato: ")
                break
            except ValueError:
                print("Por favor, ingrese un nombre válido para el segundo plato.")
        while True:
            try:
                costo_segundo_plato = float(input("Costo del segundo plato: "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido para el costo del segundo plato.")
        while True:
            try:
                bebida = input("Bebida: ")
                break
            except ValueError:
                print("Por favor, ingrese un nombre válido para la bebida.")
        while True:
            try:
                costo_bebida = float(input("Costo de la bebida: "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido para el costo de la bebida.")
        while True:
            try:
                postre = input("Postre: ")
                break
            except ValueError:
                print("Por favor, ingrese un nombre válido para el postre.")
        while True:
            try:
                costo_postre = float(input("Costo del postre: "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido para el costo del postre.")
        
        print("\n" + pedido.calcular_pedido(primer_plato, costo_primer_plato, segundo_plato, costo_segundo_plato, bebida, costo_bebida, postre, costo_postre))