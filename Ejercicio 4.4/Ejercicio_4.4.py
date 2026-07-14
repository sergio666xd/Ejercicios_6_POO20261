# Ejercicio de Polimorfismo: Profesor y ProfesorTitular

class Profesor:
    """
    Superclase que representa a un profesor genérico.
    """
    def imprimir(self) -> str:
        """Método estándar para identificar al objeto."""
        return "Es un profesor."


class ProfesorTitular(Profesor):
    """
    Subclase que representa a un profesor titular, heredando de Profesor.
    """
    def imprimir(self) -> str:
        """Sobrescribe el método imprimir de la clase padre."""
        return "Es un profesor titular."

if __name__ == "__main__":
    
    print("Simulador de Polimorfismo de Profesores\n")
    print("Este programa demuestra cómo una variable de referencia puede comportarse")
    print("de manera diferente según la clase real del objeto que se le asigne.\n")
    
    print("Seleccione qué objeto desea asignar a su referencia 'profesor':")
    print("1. Profesor Genérico (Instancia de la clase padre)")
    print("2. Profesor Titular (Instancia de la clase hija)")

    while True:
        try:
            opcion = int(input("\nIngrese el número de la opción deseada: "))
            if opcion in [1, 2]:
                break
            print("Por favor, seleccione una opción válida (1 o 2).")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    print("\nEjecutando demostración de polimorfismo...")
    print("--------------------------------------------------")

    profesor: Profesor 

    if opcion == 1:
        profesor = Profesor()
        print("Acción: profesor = Profesor()")
    else:
        profesor = ProfesorTitular()
        print("Acción: profesor = ProfesorTitular()")

    print("Llamada: profesor.imprimir()")
    print("--------------------------------------------------")
    print(f"Resultado: {profesor.imprimir()}")
    print("--------------------------------------------------")