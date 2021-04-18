from abc import ABC, abstractmethod
class Animal(ABC):
	"""docstring for Animal"""
	@abstractmethod
	def __init__(self, name, sex, age, weight, color):
		self.name = name
		self.sex = sex
		self.age = age
		self.weight = weight
		self.color = color

	@abstractmethod
	def breath(self):
		pass

	@abstractmethod
	def eat(self, food):
		pass

	@abstractmethod
	def run(self, destination):
		pass

	@abstractmethod
	def sleep(self, hours):
		pass

	@abstractmethod
	def make_sound(self):
		pass

if __name__ == '__main__':
	animal_instance = Animal("Horse", "Male", "10", 100, "Black")
	animal_instance.breath()
	animal_instance.eat("grass")
	animal_instance.run("Brazil")
	animal_instance.sleep(10)
	animal_instance.make_sound(self)

