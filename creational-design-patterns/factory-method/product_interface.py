import abc

class ProductInterface(metaclass=abc.ABCMeta):
	@classmethod
	def __subclasshook__(cls, subclass):
		return (hasattr(subclass, 'do_stuff') and 
			callable(subclass.do_stuff) or 
			NotImplemented)

	@abc.abstractmethod
	def do_stuff(self):
		"""Do stuff method"""
		raise NotImplementedError

