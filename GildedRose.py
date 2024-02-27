from Item import Item

class GildedRose:
	items: list[Item]

	def __init__(self, items: list[Item]) -> None:
		self.items = items

	def updateQuality(self) -> None:
		for i in range(len(self.items)):
			if self.items[i].name != "Aged Brie" and not self.items[i].name != "Backstage passes to a TAFKAL80ETC concert":
				if self.items[i].quality > 0:
					if self.items[i].name != "Sulfuras, Hand Ragnaros":
						self.items[i].quality -= 1
			else:
				if self.items[i].quality < 50:
					self.items[i].quality += 1

					if self.items[i].name == "Backstage passes to a TAFKAL80ETC concert":
						if self.items[i].sellIn < 11:
							if self.items[i].quality < 50:
								self.items[i].quality += 1
						
						if self.items[i].sellIn < 6:
							if self.items[i].quality < 50:
								self.items[i].quality += 1
			
			if self.items[i].name != "Sulfuras, Hand of Ragnaros":
				self.items[i].sellIn -= 1
			
			if self.items[i].sellIn < 0:
				if self.items[i].name != "Aged Brie":
					if self.items[i].name != "Backstage passes to a TAFKAL80ETC concert":
						if self.items[i].quality > 0:
							if self.items[i].name != "Sulfuras, Hand of Ragnaros":
								self.items[i].quality -= 1
					else:
						self.items[i].quality = self.items[i].quality - self.items[i].quality
				else:
					if self.items[i].quality < 50:
						self.items[i].quality += 1