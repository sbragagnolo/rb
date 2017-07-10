initialization
testStrictlyOneFailsWithGeneralHoodies
	self should: [ self findStrictlyOneProductThatMatches: {(#'product-type' -> 'hoodie')} ] raise: Error