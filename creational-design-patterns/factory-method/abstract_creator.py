from abc import ABC, abstractmethod
from product_interface import ProductInterface

class AbstractCreator(ABC):

	@abstractmethod
	def some_operation(self):
		pass

	@abstractmethod
	def create_product(self):
		pass

if __name__ == '__main__':
	abstract_creator_instance = AbstractCreator() #Wrong!
	abstract_creator_instance.some_operation()
	abstract_creator_instance.create_product()
