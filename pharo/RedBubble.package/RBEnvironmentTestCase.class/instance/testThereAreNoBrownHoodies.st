initialization
testThereAreNoBrownHoodies
	self
		assert:
			(self
				findAllProductsThatMatches:
					{(#'product-type' -> 'hoodie').
					(#options -> {(#colour -> #brown)} asDictionary)}) size
		equals: 0