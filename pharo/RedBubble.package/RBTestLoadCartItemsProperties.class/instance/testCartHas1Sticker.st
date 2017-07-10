initialization
testCartHas1Sticker
	self assert: (items select: [ :i | i selector type value = 'sticker' ] thenCollect: [ :i | i quantity ]) first equals: 1