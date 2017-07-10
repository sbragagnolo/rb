initialization
testThereAre1MediumDarkHoodie
	self
		assert:
			(self
				findAllProductsThatMatches:
					{(#'product-type' -> 'hoodie').
					(#options
						->
							{(#size -> #medium).
							(#colour -> #dark)} asDictionary)}) size
		equals: 1