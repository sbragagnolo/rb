initialization
testThereIsOneLargeWhiteHoodies
	self
		assert:
			(self
				findAllProductsThatMatches:
					{(#'product-type' -> 'hoodie').
					(#options
						->
							{(#size -> #large).
							(#colour -> #white)} asDictionary)}) size
		equals: 1