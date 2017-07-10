initialization
testThereAre4Stickers
	self assert: (self findAllProductsThatMatches: {(#'product-type' -> 'sticker')}) size equals: 4