class Item:
	name: str
	sellIn: int
	quality: int

	def __init__(self, name: str, sellIn: int, quality: int) -> None:
		self.name = name
		self.sellIn = sellIn
		self.quality = quality

	def toString(self) -> str:
		return f"{self.name}, {self.sellIn}, {self.quality}"