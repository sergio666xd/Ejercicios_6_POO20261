from abc import ABC, abstractmethod
from typing import List

class Animal(ABC):
	"""
	Clase abstracta raíz que modela un animal genérico.
	"""
	@abstractmethod
	def get_scientific_name(self) -> str:
		"""Obtiene el nombre científico del animal."""
		pass

	@abstractmethod
	def get_sound(self) -> str:
		"""Obtiene el sonido producido por el animal."""
		pass

	@abstractmethod
	def get_food(self) -> str:
		"""Obtiene el alimento que consume el animal."""
		pass

	@abstractmethod
	def get_habitat(self) -> str:
		"""Obtiene el hábitat del animal."""
		pass


class Canid(Animal, ABC):
	"""
	Subclase abstracta que representa a la familia de los cánidos.
	"""
	pass


class Feline(Animal, ABC):
	"""
	Subclase abstracta que representa a la familia de los felinos.
	"""
	pass


class Dog(Canid):
	"""Subclase concreta de Canid."""
	def get_sound(self) -> str:
		return "Ladrido"

	def get_food(self) -> str:
		return "Carnívoro"

	def get_habitat(self) -> str:
		return "Doméstico"

	def get_scientific_name(self) -> str:
		return "Canis lupus familiaris"


class Wolf(Canid):
	"""Subclase concreta de Canid."""
	def get_sound(self) -> str:
		return "Aullido"

	def get_food(self) -> str:
		return "Carnívoro"

	def get_habitat(self) -> str:
		return "Bosque"

	def get_scientific_name(self) -> str:
		return "Canis lupus"


class Lion(Feline):
	"""Subclase concreta de Feline."""
	def get_sound(self) -> str:
		return "Rugido"

	def get_food(self) -> str:
		return "Carnívoro"

	def get_habitat(self) -> str:
		return "Praderas"

	def get_scientific_name(self) -> str:
		return "Panthera leo"


class Cat(Feline):
	"""Subclase concreta de Feline."""
	def get_sound(self) -> str:
		return "Maullido"

	def get_food(self) -> str:
		return "Ratones"

	def get_habitat(self) -> str:
		return "Doméstico"

	def get_scientific_name(self) -> str:
		return "Felis silvestris catus"

if __name__ == "__main__":
	animals_list: List[Animal] = [Cat(), Dog(), Wolf(), Lion()]
	
	print("Simulador del Reino Animal (Clases Abstractas)")
	print("------------------------------------------------")
	print("Este programa demuestra cómo la abstracción impide instanciar")
	print("clases genéricas pero permite estructurar subclases concretas.")
	
	while True:
		print("\nMenú de opciones:")
		print("1. Mostrar información de todos los animales (Polimorfismo)")
		print("2. Intentar instanciar la clase abstracta 'Animal'")
		print("3. Salir")
		
		try:
			option = int(input("\nSeleccione una opción: "))
			
			if option == 1:
				print("\n==================================================")
				print("            INFORMACIÓN DE LOS ANIMALES           ")
				print("==================================================")
				for animal in animals_list:
					print(f"Nombre Científico: {animal.get_scientific_name()}")
					print(f"  └─ Sonido: {animal.get_sound()}")
					print(f"  └─ Alimentos: {animal.get_food()}")
					print(f"  └─ Hábitat: {animal.get_habitat()}")
					print("-" * 50)
					
			elif option == 2:
				print("\n[Intento]: Intentando ejecutar: 'failed_instance = Animal()'")
				try:                    failed_instance = Animal() 
				except TypeError as error:
					print("\n[¡ERROR CAPTURADO EXITOSAMENTE!]")
					print(f"Detalle del error de Python:\n-> {error}")
					print("\nExplicación: El sistema bloqueó la acción. No se puede crear")
					print("un objeto directamente de la clase abstracta 'Animal'.")
					
			elif option == 3:
				print("\n¡Gracias por usar el simulador!")
				break
			else:
				print("Opción no válida. Intente de nuevo.")
				
		except ValueError:
			print("Por favor, ingrese un número válido.")