class Animal(object):
	"""docstring for Animal"""
	def __init__(self, name, sex, age, weight, color):
		self.name = name
		self.sex = sex
		self.age = age
		self.weight = weight
		self.color = color

	def breath(self):
		print("Breathing as an Animal.")

	def eat(self, food):
		print(f"Eating {food} as an Animal.")

	def run(self, destination):
		print(f"Running to {destination} as an Animal.")

	def sleep(self, hours):
		print(f"Sleeping {hours} hours as an Animal.")


if __name__ == '__main__':
	animal_instance = Animal("Horse", "Male", "10", 100, "Black")
	animal_instance.breath()
	animal_instance.eat("grass")
	animal_instance.run("Brazil")
	animal_instance.sleep(10)

