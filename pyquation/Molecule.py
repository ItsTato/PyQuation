from .Element import Element

# Molecule(1,[Hydrogen*2]).then(1,[Oxygen*2]).then(Molecule( ... )).with(actions.HEAT).results(Molecule( H2O ))

# Molecule(3, Molecule(1,Elements.Hydrogen).add(2,Elements.Oxygen) ) -> (H2O)3

class Molecule:
	def __init__(self,elements:list[tuple[int,Element]]) -> None:
		# Molecule([ (2,Hydrogen),(1,Oxygen) ]) # This is Water H2O
		self.__elements:list[tuple[int,Element]] = elements

	@property
	def Elements(self) -> list[tuple[int,Element]]:
		return self.__elements
	@Elements.setter
	def Elements(self,new:list[tuple[int,Element]]) -> None:
		self.__elements = new
