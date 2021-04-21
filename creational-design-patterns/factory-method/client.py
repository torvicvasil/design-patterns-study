import sys
sys.path.append(".")
from abstract_creator import AbstractCreator
from product_interface import ProductInterface
from concrete_creator_a import ConcreteCreatorA
from concrete_creator_b import ConcreteCreatorB

class ProductParser(object):
	"""docstring for ProductParser"""
	def print_product_info(self, product_list):
		for product_obj in product_list:
			product_obj.do_stuff()

if __name__ == '__main__':

	creator_b = ConcreteCreatorB()
	creator_a = ConcreteCreatorA()
	
	product_list = [creator_b.create_product(), creator_a.create_product()]
	product_parser = ProductParser()
	product_parser.print_product_info(product_list)