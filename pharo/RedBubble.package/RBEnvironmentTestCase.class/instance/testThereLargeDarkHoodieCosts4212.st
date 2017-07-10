initialization
testThereLargeDarkHoodieCosts4212
	self
		assert:
			(self
				findStrictlyOneProductThatMatches:
					{(#'product-type' -> 'hoodie').
					(#options
						->
							{(#size -> #large).
							(#colour -> #dark)} asDictionary)}) basePrice
		equals: 4212