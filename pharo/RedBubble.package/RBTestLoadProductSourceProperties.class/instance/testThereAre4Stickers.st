initialization
testThereAre4Stickers
	self assert: (rawproducts select: [ : c | (c at: #'product-type' )= 'sticker' ] ) size equals: 4