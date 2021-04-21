import sys
sys.path.append(".")
from product_interface import ProductInterface

class ConcreteProductB(ProductInterface):
	def do_stuff(self):
		print("Do stuff Product B.")


if __name__ == '__main__':
	b = ConcreteProductB()
	b.do_stuff()
	print(f"issubclass(ConcreteProductB, ProductInterface): {issubclass(ConcreteProductB, ProductInterface)}")