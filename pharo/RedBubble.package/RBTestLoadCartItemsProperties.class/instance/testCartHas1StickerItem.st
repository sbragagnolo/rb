initialization
testCartHas1StickerItem
	self assert: (items select: [ :i | (i selector type value) = 'sticker' ]) size equals: 1