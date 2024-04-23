from .Element import Element

# Molecule(1,[Hydrogen*2]).then(1,[Oxygen*2]).then(Molecule( ... )).with(actions.HEAT).results(Molecule( H2O ))

# Molecule(3, Molecule(1,Elements.Hydrogen).add(2,Elements.Oxygen) ) -> (H2O)3

class Molecule:
	def __init__(self) -> None:
		pass
