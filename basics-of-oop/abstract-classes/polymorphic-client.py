import sys
sys.path.append(".")
from animal import Animal
from dog import Dog
from cat import Cat

class AnimalParser(object):
	"""docstring for Animal"""
	def print_animal_info(self, animal_list):
		for animal_obj in animal_list:
			animal_obj.breath()
			animal_obj.make_sound()

if __name__ == '__main__':
	Cat_instance = Cat("Cat", "Male", "10", 2, "Black", True)
	Dog_instance = Dog("Dog", "Male", "10", 2, "Black", True)
	animals_list = [Cat_instance, Dog_instance]
	animal_parser = AnimalParser()
	animal_parser.print_animal_info(animals_list)