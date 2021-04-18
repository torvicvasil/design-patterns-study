import sys
sys.path.append(".")
from animal import Animal

class Dog(Animal):
	"""docstring for Animal"""
	def __init__(self, name, sex, age, weight, color, isNasty):
		super().__init__(name, sex, age, weight, color)
		#or Animal.__init__(name, sex, age, weight, color)
		self._isNasty = isNasty

	@property
	def isNasty(self):
		return self._isNasty

	@isNasty.setter
	def isNasty(self, isNasty):
		if (type(isNasty) == bool):
			self._isNasty = isNasty
		else:
			print("isNasty must be bool")

	def breath(self):
		print("Breathing as a Dog.")

	def eat(self, food):
		print(f"Eating {food} as a Dog.")

	def run(self, destination):
		print(f"Running to {destination} as a Dog.")

	def sleep(self, hours):
		print(f"Sleeping {hours} hours as a Dog.")

	def bark(self):
		print(f"Barking as a Dog.")

if __name__ == '__main__':
	Dog_instance = Dog("Dog", "Male", "10", 2, "Black", True)
	Dog_instance.breath()
	Dog_instance.eat("Meat")
	Dog_instance.run("Brazil")
	Dog_instance.sleep(10)
	Dog_instance.bark()
	print(Dog_instance.isNasty)
	Dog_instance.isNasty = False
	print(Dog_instance.isNasty)
	Dog_instance.isNasty = "True"
	print(Dog_instance.isNasty)
