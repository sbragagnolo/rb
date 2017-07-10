initialization
testThereAre1SmallHoodie
	self
		assert:
			(self
				findAllProductsThatMatches:
					{(#'product-type' -> 'hoodie').
					(#options -> {(#size -> #small)} asDictionary)}) size
		equals: 1