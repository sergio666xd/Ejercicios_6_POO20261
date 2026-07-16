# Ejercicio 4.6: Métodos Polimórficos

class Teacher:
    def print_details(self):
        print("Es un profesor.")


class TenuredTeacher(Teacher):
    def __init__(self, years: int = 0):
        self.years = years

    def print_details(self):
        print("Es un profesor titular.")

    def print_years(self):
        print(f"Años = {self.years}")

if __name__ == "__main__":
    
    print("Simulador de Enlace Dinámico y Métodos Polimórficos\n")
    print("En Java, si guardas un 'TenuredTeacher' en una variable tipo 'Teacher',")
    print("el compilador bloquea las llamadas a métodos exclusivos de la clase hija.")
    print("¡Veamos qué pasa en Python!\n")
    
    years_experience = 5
    
    teacher_variable = TenuredTeacher(years=years_experience)
    
    print(f"-> Se ha creado un objeto 'TenuredTeacher' con {years_experience} años.")
    print("-> Variable asignada: 'teacher_variable'\n")
    
    print("Seleccione qué método desea intentar invocar desde la variable:")
    print("1. print_details() (Método sobrescrito, presente en ambas clases)")
    print("2. print_years()   (Método exclusivo de la clase hija, ausente en la clase padre)")

    while True:
        try:
            option = int(input("\nIngrese el número de la opción deseada: "))
            if option in [1, 2]:
                break
            print("Por favor, seleccione una opción válida (1 o 2).")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    print("\nIntentando ejecutar la llamada...")
    print("--------------------------------------------------")

    if option == 1:
        print("Llamando a: teacher_variable.print_details()")
        teacher_variable.print_details()
        print("\n[Resultado]: Funciona perfectamente en ambos lenguajes.")
        
    elif option == 2:
        print("Llamando a: teacher_variable.print_years()")
        
        print("\n--- Análisis de compatibilidad (Simulación de Compilador) ---")
        
        if hasattr(Teacher, 'print_years'):
            print("✓ El compilador aprueba la llamada porque el método existe en la clase base 'Teacher'.")
        else:
            print("✗ ERROR DE COMPILACIÓN (Estilo Java):")
            print("  La clase base 'Teacher' no tiene definido el método 'print_years'.")
            print("  El compilador no te permitiría ejecutar este programa.")

        print("\n--- Ejecución Real en Tiempo de Ejecución (Python) ---")
        try:
            teacher_variable.print_years()
            print("\n[Resultado]: ¡En Python sí funciona! Como es de tipado dinámico,")
            print("detecta que el objeto real en memoria tiene el método y lo ejecuta.")
        except AttributeError as e:
            print(f"Error en ejecución: {e}")
            
    print("--------------------------------------------------")