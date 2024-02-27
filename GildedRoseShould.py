import unittest
from GildedRose import GildedRose
from Item import Item

class TestGildedRose(unittest.TestCase):

		def test_sell_in_value_is_decreased(self) -> None:
				whatEverItem: Item = Item("whatever", 10, 0)

				gildedRose: GildedRose = GildedRose([whatEverItem])
				gildedRose.updateQuality()

				self.assertEqual(whatEverItem.sellIn, 9)

		def test_quality_value_is_decreased(self) -> None:
				whatEverItem: Item = Item("whatever", 1, 10)

				gildedRose: GildedRose = GildedRose([whatEverItem])
				gildedRose.updateQuality()

				self.assertEqual(whatEverItem.quality, 9)

		def test_quality_decreases_twice_as_much_when_sell_by_is_passed(self) -> None:
				whatEverItem: Item = Item("whatever", 0, 10)

				gildedRose: GildedRose = GildedRose([whatEverItem])
				gildedRose.updateQuality()

				self.assertEqual(whatEverItem.quality, 8)

		def test_quality_is_never_negative(self) -> None:
			whatEverItem: Item = Item("whatever", 0, 10)

			gildedRose: GildedRose = GildedRose([whatEverItem])
			gildedRose.updateQuality()

			self.assertEqual(whatEverItem.quality, 0)

		def test_aged_brie_increases_quality_with_age(self) -> None:
			agedBrie: Item = Item("Age Brie", 5, 1)

			gildedRose: GildedRose = GildedRose([agedBrie])
			gildedRose.updateQuality()

			self.assertEqual(agedBrie.quality, 2)

		def test_quality_never_increases_past_fifty(self) -> None:
				agedBrie: Item = Item("Aged Brie", 5, 50);

				gildedRose: GildedRose = GildedRose([agedBrie]);
				gildedRose.updateQuality();

				self.assertEqual(agedBrie.quality, 50);

		def testSulfurasNeverChanges(self) -> None:
				sulfuras: Item = Item("Sulfuras, Hand of Ragnaros", 0, 25);

				gildedRose: GildedRose = GildedRose([sulfuras]);
				gildedRose.updateQuality();

				self.assertEqual(sulfuras.quality, 25);
				self.assertEqual(sulfuras.sellIn, 0);

		def test_backstage_pass_increases_quality_by_one_if_sell_by_greater_then_ten(self) -> None:
				backstagePasses: Item = Item("Backstage passes to a TAFKAL80ETC concert", 11, 20);

				gildedRose: GildedRose = GildedRose([backstagePasses]);
				gildedRose.updateQuality();

				self.assertEqual(backstagePasses.quality, 21);

		def test_backstage_pass_increases_quality_by_two_if_sell_by_smaller_than_ten(self) -> None:
				backstagePasses: Item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 20);

				gildedRose: GildedRose = GildedRose([backstagePasses]);
				gildedRose.updateQuality();

				self.assertEqual(backstagePasses.quality, 22);

		def test_backstage_pass_increases_quality_by_three_if_sell_by_smaller_than_five(self) -> None:
				backstagePasses: Item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 20);

				gildedRose: GildedRose = GildedRose([backstagePasses]);
				gildedRose.updateQuality();

				self.assertEqual(backstagePasses.quality, 23);

		def test_backstage_pass_loses_value_after_sell_by_passes(self) -> None:
				backstagePasses: Item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 20);

				gildedRose: GildedRose = GildedRose([backstagePasses]);
				gildedRose.updateQuality();

				self.assertEqual(backstagePasses.quality, 0);

if __name__ == '__main__':
		unittest.main()