initialization
testCartHas1StickerItem
	self assert: (rawitems select: [ :i | (i at: #'product-type') = 'sticker' ]) size equals: 1