import abc

class AnimalInterface(metaclass=abc.ABCMeta):
	@classmethod
	def __subclasshook__(cls, subclass):
		return (hasattr(subclass, 'breath') and 
			callable(subclass.breath) and 
			hasattr(subclass, 'eat') and 
			callable(subclass.eat) and 
			hasattr(subclass, 'run') and 
			callable(subclass.run) and 
			hasattr(subclass, 'sleep') and 
			callable(subclass.sleep)  and 
			hasattr(subclass, 'make_sound') and 
			callable(subclass.make_sound) or 
			NotImplemented)

	@abc.abstractmethod
	def breath(self):
		"""Breath method"""
		raise NotImplementedError

	@abc.abstractmethod
	def eat(self, food: str):
		"""Eat method"""
		raise NotImplementedError

	@abc.abstractmethod
	def run(self, destination: str):
		"""Run method"""
		raise NotImplementedError

	@abc.abstractmethod
	def sleep(self, hours: float):
		"""Sleep method"""
		raise NotImplementedError

	@abc.abstractmethod
	def make_sound(self):
		"""Sleep method"""
		raise NotImplementedError
