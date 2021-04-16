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

	def meow(self):
		print(f"Meowing as a Cat.")

if __name__ == '__main__':
	cat_instance = Cat("Cat", "Male", "10", 2, "Black", True)
	cat_instance.breath()
	cat_instance.eat("Fish")
	cat_instance.run("Brazil")
	cat_instance.sleep(10)
	cat_instance.meow()
	print(cat_instance.isNasty)
	cat_instance.isNasty = False
	print(cat_instance.isNasty)
	cat_instance.isNasty = "True"
	print(cat_instance.isNasty)
