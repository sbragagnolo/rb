initialization
testExampleCartTotalPriceIs
	| smallStickerPrice smallDarkHoodiesPrice |
	smallStickerPrice := 1 * (221 + (221 * 0.1) rounded).
	smallDarkHoodiesPrice := 2 * (3800 + (3800 * 0.2) rounded).
	self assert: cart price equals: smallStickerPrice + smallDarkHoodiesPrice