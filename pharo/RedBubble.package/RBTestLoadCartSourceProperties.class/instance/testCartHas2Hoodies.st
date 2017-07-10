initialization
testCartHas2Hoodies
	 self assert: (rawitems select: [ : i |( i at: #'product-type' ) ='hoodie' ] thenCollect:[: i | i at: #quantity ]) first equals: 2