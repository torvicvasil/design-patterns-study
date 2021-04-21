import sys
sys.path.append(".")
from abstract_creator import AbstractCreator
from concrete_product_b import ConcreteProductB


class ConcreteCreatorB(AbstractCreator):

	def some_operation(self):
		print("Do some operation.")


	def create_product(self):
		return ConcreteProductB()
		

if __name__ == '__main__':
	creator_b = ConcreteCreatorB()
	creator_b.some_operation()
	product_b = creator_b.create_product()
	product_b.do_stuff()