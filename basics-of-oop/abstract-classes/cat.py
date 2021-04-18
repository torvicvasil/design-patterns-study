import sys
sys.path.append(".")
from animal import Animal

class Cat(Animal):
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
		print("Breathing as a Cat.")

	def eat(self, food):
		print(f"Eating {food} as a Cat.")

	def run(self, destination):
		print(f"Running to {destination} as a Cat.")

	def sleep(self, hours):
		print(f"Sleeping {hours} hours as a Cat.")

	def _meow(self):
		return "Meow"

	def make_sound(self):
		print(self._meow())


if __name__ == '__main__':
	Cat_instance = Cat("Cat", "Male", "10", 2, "Black", True)
	Cat_instance.breath()
	Cat_instance.eat("Fish")
	Cat_instance.run("Brazil")
	Cat_instance.sleep(10)
	Cat_instance.make_sound()
	print(Cat_instance.isNasty)
	Cat_instance.isNasty = False
	print(Cat_instance.isNasty)
	Cat_instance.isNasty = "True"
	print(Cat_instance.isNasty)
