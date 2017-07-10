initialization
testThereAre5Hoodies
	self
		assert: (self findAllProductsThatMatches: {(#'product-type' -> 'hoodie')} ) size
		equals: 5