import sys
sys.path.append(".")
from abstract_creator import AbstractCreator
from concrete_product_a import ConcreteProductA


class ConcreteCreatorA(AbstractCreator):

	def some_operation(self):
		print("Do some operation.")


	def create_product(self):
		return ConcreteProductA()
		

if __name__ == '__main__':
	creator_a = ConcreteCreatorA()
	creator_a.some_operation()
	product_a = creator_a.create_product()
	product_a.do_stuff()