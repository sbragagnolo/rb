initialization
testThereAre1MediumWhiteHoodie
	self
		assert:
			(self
				findAllProductsThatMatches:
					{(#'product-type' -> 'hoodie').
					(#options
						->
							{(#size -> #medium).
							(#colour -> #white)} asDictionary)}) size
		equals: 1