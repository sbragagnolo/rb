initialization
testThereIs1Leggings
	self assert: (self findAllProductsThatMatches: {(#'product-type' -> 'leggings')}) size equals: 1