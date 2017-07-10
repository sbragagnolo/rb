initialization
testCartHas2Hoodies
	 self assert: (items select: [ : i |i selector type value='hoodie' ] thenCollect:[: i | i quantity ]) first equals: 2