initialization
testThereLargeWhiteHoodieCosts3848
	self
		assert:
			(self
				findStrictlyOneProductThatMatches:
					{(#'product-type' -> 'hoodie').
					(#options
						->
							{(#size -> #large).
							(#colour -> #white)} asDictionary)}) basePrice
		equals: 3848