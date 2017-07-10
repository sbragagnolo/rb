initialization
testCartHas1HoodieItem
	 self assert: (rawitems select: [ : i |( i at: #'product-type' ) ='hoodie' ]) size equals: 1