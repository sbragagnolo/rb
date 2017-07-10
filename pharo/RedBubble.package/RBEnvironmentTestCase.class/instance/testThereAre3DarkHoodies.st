initialization
testThereAre3DarkHoodies
	self
		assert:
			(self
				findAllProductsThatMatches:
					{(#'product-type' -> 'hoodie').
					(#options -> {(#colour -> #dark)} asDictionary)}) size
		equals: 3