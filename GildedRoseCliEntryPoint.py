import sys
from GildedRose import GildedRose
from Item import Item



def main(args: list):
	print("OMGHAI!")

	items: list[Item] = [
		Item("+5 Dexterity Vest", 10, 20),
		Item("Aged Brie", 2, 0),
		Item("Elixir of the Mongoose", 5, 7),
		Item("Sulfuras, Hand of Ragnaros", 0, 80),
		Item("Sulfuras, Hand of Ragnaros", -1, 80),
		Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
		Item("Backstage passes to a TAFKAL80ETC concert", 10, 49),
		Item("Backstage passes to a TAFKAL80ETC concert", 5, 49),
		#this conjured item does not work properly yet
		Item("Conjured Mana Cake", 3, 6)
	]

	app = GildedRose(items)

	days: int = 2
	if len(args) > 0:
		days = int(args[0]) + 1
	
	for i in range(days):
		print(f"-------- day {i} --------")
		print("name, sellIn, quality")
		for item in items:
			print(item.toString())
		print()
		app.updateQuality()

if __name__ == "__main__":
	main(sys.argv[1:])