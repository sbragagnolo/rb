initialization
testThereAre5Hoodies
	self assert: (rawproducts select: [ : c | (c at: #'product-type' )= 'hoodie' ] ) size equals: 5