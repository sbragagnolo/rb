initialization
testThereAre2LargeHoodies
	self
		assert:
			(self
				findAllProductsThatMatches:
					{(#'product-type' -> 'hoodie').
					(#options -> {(#size -> #large)} asDictionary)}) size
		equals: 2