initialization
testThereAreNoSandals
	self assert: (self findAllProductsThatMatches: {(#'product-type' -> 'sandals')}) size equals: 0