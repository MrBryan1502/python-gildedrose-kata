from Item import Item

class GildedRose:

	_AGED_BRIE: str = "Aged Brie"
	_BACKSTAGE_PASSES: str = "Backstage passes to a TAFKAL80ETC concert"
	_SULFURAS: str = "Sulfuras, Hand of Ragnaros"
	_AGED_BRIE_DOUBLE_QUALITY_DECREMENT_SELL_IN_THRESHOLD: int = int(0)
	_BACKSTAGE_PASSES_DOUBLE_QUALITY_INCREASE_SELL_IN_THRESHOLD: int = int(10)
	_BACKSTAGE_PASSES_TRIPLE_QUALITY_INCREASE_SELL_IN_THRESHOLD: int = int(5)
	_BACKSTAGE_PASSES_QUALITY_RESET_SELL_IN_THRESHOLD: int = int(0)
	_DEFAULT_ITEM_DOUBLE_QUALITY_DECREASE_SELL_IN_THRESHOLD: int = int(0)
	_MAX_QUALITY: int = int(50)
	_MIN_QUALITY: int = int(0)

	_items: list[Item]

	def __init__(self, items: list[Item]) -> None:
		self._items = items

	def updateQuality(self) -> None:
		for item in self._items:
			if item.name == self._AGED_BRIE:
				self._decreaseSellIn(item)
				self._updateAgedBrieQuality(item)
			elif item.name == self._BACKSTAGE_PASSES:
				self._decreaseSellIn(item)
				self._updateBackstagePassesQuality(item)
			elif item.name == self._SULFURAS:
				pass
			else:
				self._decreaseSellIn(item)
				self._updateDefaultItemQuality(item)

	def _decreaseSellIn(item: Item) -> None:
		item.sellIn -= 1

	def _updateAgedBrieQuality(self, item: Item) -> None:
		self._increaseQuality(item)

		if item.sellIn < self._AGED_BRIE_DOUBLE_QUALITY_DECREMENT_SELL_IN_THRESHOLD:
			self._increaseQuality(item)

	def _updateBackstagePassesQuality(self, item: Item) -> None:
		self._increaseQuality(item)

		if item.sellIn < self._BACKSTAGE_PASSES_DOUBLE_QUALITY_INCREASE_SELL_IN_THRESHOLD:
			self._increaseQuality(item)
		if item.sellIn < self._BACKSTAGE_PASSES_TRIPLE_QUALITY_INCREASE_SELL_IN_THRESHOLD:
			self._increaseQuality(item)
		if item.sellIn < self._BACKSTAGE_PASSES_QUALITY_RESET_SELL_IN_THRESHOLD:
			self._resetQuality(item)

	def _updateDefaultItemQuality(self, item: Item) -> None:
		self._decreaceQuality(item)

		if item.sellIn < self._DEFAULT_ITEM_DOUBLE_QUALITY_DECREASE_SELL_IN_THRESHOLD:
			self._decreaceQuality(item)

	def _resetQuality(item: Item) -> None:
		item.quality = 0

	def _increaseQuality(self, item: Item) -> None:
		if item.quality < self._MAX_QUALITY:
			item.quality += 1
		
	def _decreaceQuality(self, item: Item) -> None:
		if item.quality > self._MIN_QUALITY:
			item.quality -= 1