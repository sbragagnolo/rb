initialization
testThereAre1MediumHoodie
	self
		assert:
			(self
				findAllProductsThatMatches:
					{(#'product-type' -> 'hoodie').
					(#options -> {(#size -> #medium)} asDictionary)}) size
		equals: 1