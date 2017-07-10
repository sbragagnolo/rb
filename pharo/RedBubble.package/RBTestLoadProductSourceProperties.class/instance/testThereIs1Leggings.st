initialization
testThereIs1Leggings
	self assert: (rawproducts select: [ : c | (c at: #'product-type' )= 'leggings' ] ) size equals: 1