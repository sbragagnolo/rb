initialization
testCartHas1HoodieItem
	self assert: (items select: [ :i | i selector type value = 'hoodie' ]) size equals: 1