initialization
testThereAre3WhiteHoodies
	self
		assert:
			(self
				findAllProductsThatMatches:
					{(#'product-type' -> 'hoodie').
					(#options -> {(#colour -> #white)} asDictionary)}) size
		equals: 3