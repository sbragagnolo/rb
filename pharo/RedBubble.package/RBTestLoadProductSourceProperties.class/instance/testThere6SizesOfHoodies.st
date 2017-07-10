initialization
testThere6SizesOfHoodies
	self
		assert:
			((rawproducts select: [ :c | (c at: #'product-type') = 'hoodie' ])
				flatCollectAsSet: [ :c | 
					((c at: #options) at: #size) isString
						ifTrue: [ {((c at: #options) at: #size)} ]
						ifFalse: [ (c at: #options) at: #size ] ]) asSet size
		equals: 6