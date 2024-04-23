class Element:
	def __init__(self,name:str,symbol:str,atomic_number:int,atomic_mass:float) -> None:
		self._name:str = name.lower().capitalize()
		self._symbol:str = symbol.lower().capitalize()
		self._atomic:int = atomic_number
		self._mass:float = atomic_mass
		return
	@property
	def Name(self) -> str:
		return self._name
	@Name.setter
	def Name(self,name:str) -> None:
		self._name = name.lower().capitalize()
	
	@property
	def Symbol(self) -> str:
		return self._symbol
	@Symbol.setter
	def Symbol(self,symbol:str) -> None:
		self._symbol = symbol.lower().capitalize()

	@property
	def Atomic_Number(self) -> int:
		return self._atomic
	@Atomic_Number.setter
	def Atomic_Number(self,atomic_number:int) -> None:
		self._atomic = atomic_number
	
	@property
	def Atomic_Mass(self) -> float:
		return self._mass
	@Atomic_Mass.setter
	def Atomic_Mass(self,atomic_mass:float) -> None:
		self._mass = atomic_mass