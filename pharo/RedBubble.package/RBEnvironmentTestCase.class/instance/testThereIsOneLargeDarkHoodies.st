initialization
testThereIsOneLargeDarkHoodies
	self
		assert:
			(self
				findAllProductsThatMatches:
					{(#'product-type' -> 'hoodie').
					(#options
						->
							{(#size -> #large).
							(#colour -> #dark)} asDictionary)}) size
		equals: 1