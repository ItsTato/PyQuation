class Element:
	def __init__(self,name:str,symbol:str,atomic_number:int,atomic_mass:float) -> None:
		self.__name:str = name.lower().capitalize()
		self.__symbol:str = symbol.lower().capitalize()
		self.__atomic:int = atomic_number
		self.__mass:float = atomic_mass
		return
	@property
	def Name(self) -> str:
		return self.__name
	@Name.setter
	def Name(self,name:str) -> None:
		self.__name = name.lower().capitalize()
	
	@property
	def Symbol(self) -> str:
		return self.__symbol
	@Symbol.setter
	def Symbol(self,symbol:str) -> None:
		self.__symbol = symbol.lower().capitalize()

	@property
	def Atomic_Number(self) -> int:
		return self.__atomic
	@Atomic_Number.setter
	def Atomic_Number(self,atomic_number:int) -> None:
		self.__atomic = atomic_number
	
	@property
	def Atomic_Mass(self) -> float:
		return self.__mass
	@Atomic_Mass.setter
	def Atomic_Mass(self,atomic_mass:float) -> None:
		self.__mass = atomic_mass