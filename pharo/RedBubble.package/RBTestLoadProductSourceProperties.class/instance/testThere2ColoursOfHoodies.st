initialization
testThere2ColoursOfHoodies
	self
		assert:
			((rawproducts select: [ :c | (c at: #'product-type') = 'hoodie' ])
				flatCollectAsSet: [ :c | 
					((c at: #options) at: #colour) isString
						ifTrue: [ {((c at: #options) at: #colour)} ]
						ifFalse: [ (c at: #options) at: #colour ] ]) asSet size
		equals: 2