import sys
sys.path.append(".")
from product_interface import ProductInterface

class ConcreteProductA(ProductInterface):
	def do_stuff(self):
		print("Do stuff Product A.")


if __name__ == '__main__':
	a = ConcreteProductA()
	a.do_stuff()
	print(f"issubclass(ConcreteProductA, ProductInterface): {issubclass(ConcreteProductA, ProductInterface)}")